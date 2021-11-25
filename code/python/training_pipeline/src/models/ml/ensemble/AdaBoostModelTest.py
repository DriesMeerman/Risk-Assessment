import math
from typing import Dict
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

from models.ml.ensemble.EnsembleModelTest import *
from sklearn.ensemble import AdaBoostClassifier


class AdaBoostModelTest(EnsembleModelTest):
    def __init__(self, training_df: pd.DataFrame, config, feature_variation: str) -> None:
        super().__init__(training_df, config, feature_variation)
        self.name = "AdaBoost"
        self.name_short = "ADB"

    def train_model(self):
        pass

    def optimize_config(self):
        hyper_parameters = {
            'n_estimators': [50, 100],
            'base_estimator': [DecisionTreeClassifier(), LogisticRegression()]
        }
        self.optimize_config_stub(hyper_parameters, AdaBoostClassifier())

    @staticmethod
    def get_model(frame: pd.DataFrame, config, variation: str) -> ModelTest:
        return AdaBoostModelTest(frame, config, variation)
