import numpy as np
from sklearn.base import BaseEstimator, RegressorMixin, ClassifierMixin
from tensorflow.python.keras import Model
from tensorflow.python.keras.layers import Dense, Input, LeakyReLU, Dropout, Add, Activation, Lambda, ELU, Multiply, Reshape, PReLU, Flatten, Concatenate
import tensorflow as tf
import math
import tensorflow.python.keras.backend as K
from transformers import TFAutoModel, AutoTokenizer
from hashlib import md5
from utils.temporal_filter import TemporalFilter
import json
import os


def get_feed_forward_model(num_inputs=1024, num_outputs=1, sequence_model=False):

    if not sequence_model:

        # Traditional flat NN with a finite set of inputs

        inputs = Input(shape=(num_inputs,))
        outputs = Dropout(rate=0.5)(inputs)

    else:

        # Sequence encoder model with input of arbitrary length

        inputs = Input(shape=(None, num_inputs))
        outputs = Dropout(rate=0.5, noise_shape=(None, 1, num_inputs))(inputs)  # Remove features (from all positions)
        outputs = Dense(int(math.sqrt(inputs.shape[-1])))(outputs)  # Select from/transform pre-trained embeddings
        outputs = Lambda(lambda x: tf.linalg.norm(x, axis=-2))(outputs)  # Pool over tokens

    # Common part

    outputs = Dense(num_outputs)(outputs)
    outputs = Lambda(lambda x: tf.expand_dims(x, axis=-1) * tf.expand_dims(x, axis=-2), output_shape=(None, num_outputs, num_outputs))(outputs)
    outputs = Flatten()(outputs)
    outputs = Lambda(lambda x: K.l2_normalize(x, axis=-1))(outputs)
    outputs = PReLU()(outputs)
    outputs = Dropout(rate=0.5)(outputs)

    # Generate final output

    outputs = Dense(num_outputs)(outputs)
    outputs = Activation("sigmoid")(outputs)

    return Model(inputs, outputs)


def log_loss(y_true, y_pred):
    ll = y_true * tf.math.log(y_pred + 0.0000001) + (1.0 - y_true) * tf.math.log((1.0 - y_pred) + 0.0000001)
    return - tf.reduce_mean(ll)


def hinge_loss(y_true, y_pred):

    y_pred = y_pred * 2.0 - 1.0
    y_true = y_true * 2.0 - 1.0

    return tf.reduce_mean(tf.maximum(0.0, 1.0 - y_true * y_pred))


def rank_loss(y_true, y_pred):

    y_pred_diffs = (tf.expand_dims(y_pred, -1) - tf.expand_dims(y_pred, -2))
    y_true_diffs = (tf.expand_dims(y_true, -1) - tf.expand_dims(y_true, -2))

    rank_correspondence = - tf.abs(y_pred_diffs - y_true_diffs)
    position_correspondence = - tf.abs(y_pred - y_true)

    return - tf.reduce_mean(rank_correspondence) - tf.reduce_mean(position_correspondence) / tf.cast(tf.shape(y_pred)[-1], tf.float32)


def correlation_loss(y_true, y_pred):

    y_pred_normalized = (y_pred - 0.5) / (tf.math.reduce_std(y_pred, axis=0) + 0.0000001)

    correlation = y_pred_normalized * (y_true - 0.5)

    return - tf.reduce_mean(correlation)


def tau(y_true, y_pred):

    y_pred = (tf.expand_dims(y_pred, -1) - tf.expand_dims(y_pred, -2))
    y_true = (tf.expand_dims(y_true, -1) - tf.expand_dims(y_true, -2))
    correspondence = tf.sign(y_pred) * tf.sign(y_true)
    weight = tf.abs(y_true)

    return tf.square(tf.reduce_sum(correspondence * weight) / tf.reduce_sum(weight))


class KerasEstimator(BaseEstimator, RegressorMixin, ClassifierMixin):

    '''
    An sklearn compatible black-box estimator based on Keras which tackles a variety of problem types, including text
    classification.
    '''

    DEFAULT_TRANSFORMER = "t5-large"
    transformer_tokenizer = None
    transformer_encoder = None
    try:
        cached_text = np.load(str(DEFAULT_TRANSFORMER) + "_feature_cache.npy", allow_pickle=True).item()
    except:
        cached_text = {}

    def __init__(self, model_config=None):
        if model_config is None:
            self.model = None
        if model_config:
            with open(model_config) as config_file:
                config = json.load(config_file)
            self.model = get_feed_forward_model(config["num_inputs"], config["num_outputs"], sequence_model=config["sequence_model"])
            self.model.load_weights(config["weights_file"])


    def get_params(self, deep=True):
        return {}

    def set_params(self, **parameters):
        for parameter, value in parameters.items():
            setattr(self, parameter, value)
        return self

    def _encode_text(self, X):

        if not isinstance(X, list):
            X = X.tolist()

        # Get a tokenizer singleton
        if self.transformer_tokenizer is None:
            self.transformer_tokenizer = AutoTokenizer.from_pretrained(self.DEFAULT_TRANSFORMER)

        # Get a transformer singleton
        if self.transformer_encoder is None:
            self.transformer_encoder = TFAutoModel.from_pretrained(self.DEFAULT_TRANSFORMER)
            if hasattr(self.transformer_encoder, "encoder"):
                self.transformer_encoder = self.transformer_encoder.encoder

        X_processed = np.zeros(shape=(len(X), 512, 1024))

        cache_updated = False

        for index in range(len(X)):
            x = X[index]

            # Retrieve or create the text embedding
            hash_x = md5(x.encode()).hexdigest()
            if hash_x not in self.cached_text:
                print("Encoding instance text: " + str(index + 1) + "/" + str(len(X)))
                tokens = self.transformer_tokenizer([x], return_tensors="tf", truncation=True, max_length=512)
                x = self.transformer_encoder(**tokens).last_hidden_state.numpy()[0]
                self.cached_text[hash_x] = x
                cache_updated = True
            else:
                print("Retrieving cached instance encoding: " + str(index + 1) + "/" + str(len(X)))
                x = self.cached_text[hash_x]

            X_processed[index] = np.pad(x, [[0, 512 - x.shape[-2]], [0, 0]])

        if cache_updated:
            np.save(str(self.DEFAULT_TRANSFORMER) + "_feature_cache.npy", self.cached_text)

        return X_processed

    def fit(self, X, Y, sample_weight=None, min_train_loss=None, max_batches=None):

        '''
        Fit a model to the data.
        :param X: A 2D-array of numeric features (for flat problems), or a 1D array of strings (for text problems)
        :param Y: A 2D-array of target values, in the range 0-1. For classfication problems use 0 and 1. For regression map domain to the unit interval.
        :param sample_weight: An optional 1D array of weights indicating the importance of each instance.
        :param min_train_loss: Training will be stopped early if the training loss dips below this value (derive using fit_CV())
        :param max_iterations: Training will be stopped early after this number of batches (derive using fit_CV())
        :return: N/A
        '''

        if isinstance(X[0], str):
            X = self._encode_text(X)

            self.model: Model = get_feed_forward_model(len(X[0][0]), len(Y[0]), sequence_model=True)
        else:
            self.model: Model = get_feed_forward_model(len(X[0]), len(Y[0]), sequence_model=False)
        self.model.compile("adam", log_loss, metrics=tau)

        Y = np.array(Y)
        Y = np.array(Y)
        Y -= np.min(Y, axis=0)
        Y /= np.max(Y, axis=0)

        num_instances = len(X)
        batch_size = int(math.sqrt(num_instances))
        if max_batches is None:
            num_batches = int(max_batches * 1.75)

        for batch in range(max_batches):
            indices = np.random.choice(num_instances, size=batch_size)
            X_sample = X[indices]
            Y_sample = Y[indices]
            if sample_weight is not None:
                weight_sample = sample_weight[indices]
            else:
                weight_sample = None
            train_loss = self.model.train_on_batch(X_sample, Y_sample, sample_weight=weight_sample)

            if min_train_loss is not None and train_loss < min_train_loss:
                break

        self.model.save_weights("model_weights.h5")

    def fit_CV(self, X, Y, sample_weight=None, num_folds=10):

        '''
        Fit multiple models to subsets of the data, to robustly understand expected model performance and establish appropriate hyper-parameters
        :param X: As for fit()
        :param Y: As for fit()
        :param sample_weight: As for fit()
        :param num_folds: Number of subsets to split data into. Higher values result in better estimates. Default is 10.
        :return: {
                    "Y_hat": Predictions generated by cross-validation. Compare with Y to understand expected model performance.
                    "optimum_batches": The number of batches at which stop training for best out-of-sample performance. Use with fit()
                    "optimum_train_loss": The training loss below which to stop training for best out-of-sample performance. Use with fit()
                 }
        '''

        if isinstance(X[0], str):
            X = self._encode_text(X)
            input_is_text = True
        else:
            input_is_text = False

        train_weight = None
        test_weight = None

        Y = np.array(Y)
        Y = np.array(Y)
        Y -= np.min(Y, axis=0)
        Y /= np.max(Y, axis=0)
        Y_hat = np.zeros_like(Y)

        for fold in range(num_folds):

            test_indices = range(len(X))[fold::num_folds]
            train_indices = [i for i in range(len(X)) if i not in test_indices]

            train_X = X[train_indices]
            train_Y = Y[train_indices]
            test_X = X[test_indices]
            test_Y = Y[test_indices]

            if sample_weight is not None:
                train_weight = sample_weight[train_indices]
                test_weight = sample_weight[test_indices]

            if input_is_text:
                model: Model = get_feed_forward_model(len(X[0][0]), len(Y[0]), sequence_model=True)
            else:
                model: Model = get_feed_forward_model(len(X[0]), len(Y[0]), sequence_model=False)
            model.compile("adam", log_loss, metrics=tau)

            num_instances = len(train_X)
            sample_size = int(math.sqrt(len(X)))
            num_batches = int(num_instances * 1.75)

            training_loss_filter = [TemporalFilter(), TemporalFilter()]
            test_loss_filter = [TemporalFilter(), TemporalFilter()]

            for batch in range(num_batches):
                batch_indices = np.random.choice(num_instances, size=sample_size)
                X_sample = train_X[batch_indices]
                Y_sample = train_Y[batch_indices]
                if train_weight is not None:
                    weight_sample = train_weight[batch_indices]
                else:
                    weight_sample = None
                train_loss = model.train_on_batch(X_sample, Y_sample, sample_weight=weight_sample)
                test_loss = model.test_on_batch(test_X, test_Y, sample_weight=test_weight)

                [filter.add(loss) for filter, loss in zip(training_loss_filter, train_loss)]
                [filter.add(loss) for filter, loss in zip(test_loss_filter, test_loss)]
                filtered_training_loss = [filter.get_estimate() for filter in training_loss_filter]
                filtered_test_loss = [filter.get_estimate() for filter in test_loss_filter]

                print(
                    str(fold + 1) +
                    "\t" + str(batch + 1) +
                    "\t" + str(filtered_training_loss[0]) + "\t" + str(filtered_test_loss[0]) +
                    "\t" + str(filtered_training_loss[1]) + "\t" + str(filtered_test_loss[1])
                )

            Y_hat[test_indices] = model.predict_on_batch(test_X)
            model.save_weights("model_weights_fold_" + str(fold + 1) + "of" + str(num_folds) + ".h5")

        return Y_hat  # [TO DO] return additional metrics

    def predict(self, X):

        if isinstance(X[0], str):
            X = self._encode_text(X)
        y_hat = self.model.predict(X)
        return y_hat

    def predict_proba(self, X):

        return self.predict(X)
