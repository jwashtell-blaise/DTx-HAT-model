import numpy as np

class TemporalFilter():

    '''
    A simple online 1D filter for creating a moving average which adapts to the level of drift vs noise in the signal.
    Useful for smoothing estimating batch-to-batch losses during training.
    '''

    def __init__(self):
        self.values = []

    def add(self, value):
        self.values.append(value)

    def get_estimate(self):
        if len(self.values) <= 2:
            return self.values[-1]
        else:
            estimates = [np.mean(self.values[start:], axis=-1) for start in range(3)]
            biases = [np.mean(estimates[start] - self.values[start:], axis=-1) for start in range(3)]
            best = np.argmin(np.abs(biases))
            self.values = self.values[best:]
            return estimates[best]

    def get_size(self):
        return len(self.values)