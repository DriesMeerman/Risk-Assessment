import math
from typing import Dict
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

from models.ml.ensemble.EnsembleModelTest import *


class GradientBoostModelTest(EnsembleModelTest):
    def __init__(self, training_df: pd.DataFrame, config, feature_variation: str) -> None:
        super().__init__(training_df, config, feature_variation)
        self.name = "GradientBoost"
        self.name_short = "GB"

    def train_model(self):
        pass

    def optimize_config(self):
        hyper_parameters = {
            'n_estimators': [50, 100],
            'max_features': ['auto', 'sqrt', 'log2'],
            'criterion': ['friedman_mse', 'squared_error', 'mse'],
            'loss': ['deviance', 'exponential']
        }
        self.optimize_config_stub(hyper_parameters, GradientBoostingClassifier())

    @staticmethod
    def get_model(frame: pd.DataFrame, config, variation: str) -> ModelTest:
        return GradientBoostModelTest(frame, config, variation)
