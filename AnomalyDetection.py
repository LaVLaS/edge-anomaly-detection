import logging
import os, sys
import time

_LOGGER = logging.getLogger()
_LOGGER.setLevel(logging.INFO)

class AnomalyDetection(object):
    def __init__(self):
        self.threshold = int(os.environ.get('MODEL_THRESHOLD', 0))

    def predict(self, X, feature_names):
        print(X)
        return [1] if X[0] >= self.threshold else [0]
