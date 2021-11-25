import time
from typing import Dict
import pandas as pd
from sklearn.svm import SVC

from .ModelTest import ModelTest, ConfigHelper


class SVCModelTest(ModelTest):
    def __init__(self, training_df: pd.DataFrame, config: ConfigHelper, variation: str) -> None:
        super().__init__(training_df, config, variation)
        self.name = "Support Vector Machine (classifier)"
        self.name_short = "SVC"

    def train_model(self):
        kernel = "rbf"

        self.logger.debug("Start training {}.".format(kernel))
        start = time.time()
        model = SVC(kernel=kernel, probability=True)
        model.fit(self.X_train, self.y_train)
        self.logger.debug("Fit model in {} seconds".format(round(time.time() - start, 2)))
        self.model = model
        self.calc_accuracy()

    def optimize_config(self):
        hyper_parameters = {
            'kernel': ['sigmoid', 'linear', 'poly', 'rbf'],
            'class_weight': ['balanced', None],
            'gamma': ['scale', 'auto']
        }

        self.optimize_config_stub(hyper_parameters, SVC(probability=True))

    @staticmethod
    def get_model(frame, config: ConfigHelper, variation: str):
        return SVCModelTest(frame, config, variation)
