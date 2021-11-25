import math
from typing import Dict
import pandas as pd
from sklearn.ensemble import BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

from models.ml.ensemble.EnsembleModelTest import *


class BaggingModelTest(EnsembleModelTest):
    def __init__(self, training_df: pd.DataFrame, config, feature_variation: str) -> None:
        super().__init__(training_df, config, feature_variation)
        self.name = "Bagging"
        self.name_short = "BAG"

    def train_model(self):
        pass

    def optimize_config(self):
        hyper_parameters = {
            'n_estimators': [10, 20, 50],
            'base_estimator': [DecisionTreeClassifier(), KNeighborsClassifier()],
            'max_samples': [1.0, 0.75, 0.5],
            'max_features': [1.0, 0.75, 0.5]
        }
        self.optimize_config_stub(hyper_parameters, BaggingClassifier())

    @staticmethod
    def get_model(frame: pd.DataFrame, config, variation: str) -> ModelTest:
        return BaggingModelTest(frame, config, variation)