from keras_estimator import KerasEstimator
from collections import defaultdict
from task_specific_resources.HAT_category_mapping import category_mapping
from utils.mapping import map_few_hot
import numpy as np


# Retrieve data

inputs = {}
targets = defaultdict(lambda: [])

# Prepare training data

categories = set()
for source_category, target_category in category_mapping:
    categories.add(target_category)
categories = sorted(list(categories))

for instance in data:

    if instance["canonical"]["_id"] not in inputs:  # Disregard duplicate case IDs for purpose of constructing input
        inputs[instance["canonical"]["_id"]] =\
            "\n".join([instance["canonical"]["SelfAssessment_" + str(q)] for q in range(11)])  # Join all SAQ responses

    one_hot = map_few_hot(instance["canonical"], category_mapping)
    targets[instance["canonical"]["_id"]].append(one_hot)  # When constructing targets aggregate annotations by case ID

supervised_inputs = [inputs[user] for user in sorted(inputs.keys())]
supervised_targets = [targets[user] for user in sorted(targets.keys())]

# Prepare arrays for training

X = []
Y = []
weights = []
for x, y in zip(supervised_inputs, supervised_targets):
    X.append(x)
    Y.append(np.mean(y, axis=0))  # Average over annotions to get coarse probability of label
    weights.append(len(y))

estimator = KerasEstimator()

'''
When solving a new problem/dataset, use fit_CV() in first instance to understand performance and identify appropriate
hyper-parameters to use with fit().  When retraining on same data, or doing inconsequential updates, just use fit().

outputs = estimator.fit_CV(X, Y, sample_weight=None, num_folds=20)
'''

estimator.fit(X, Y, sample_weight=None)
estimator.model.save_weights("task_specific_resources/model_weights.h5")