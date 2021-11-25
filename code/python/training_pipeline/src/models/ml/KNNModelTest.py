import time
from typing import Dict
from .ModelTest import ModelTest
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from ..config_helper import ConfigHelper


class KNNModelTest(ModelTest):
    def __init__(self, training_df: pd.DataFrame, config, variation: str) -> None:
        super().__init__(training_df, config=config, feature_variation=variation)
        self.name = "k-Nearest Neighbour"
        self.name_short = "KNN"
        self.k = 20

    def train_model(self):
        raise Exception('train model still used somehow')
        # K = self.k
        #
        # self.logger.debug("Start training with a K of {}.".format(K))
        # start = time.time()
        # model = KNeighborsClassifier(n_neighbors=K)
        # model.fit(self.X_train, self.y_train)
        # fit_time = time.time() - start
        # self.best_mean_fit_time = fit_time
        # self.logger.debug("Fit model in {} seconds".format(round(fit_time, 2)))
        # self.model = model
        # self.calc_accuracy()

    def optimize_config(self):
        range_end = self.k
        hyper_parameters = {
            'n_neighbors': range(1, range_end + 1),
            'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute'],
            'weights': ['uniform', 'distance']
        }

        self.optimize_config_stub(hyper_parameters, KNeighborsClassifier())

    @staticmethod
    def get_model(frame: pd.DataFrame, config: ConfigHelper, variation: str):
        return KNNModelTest(frame, config, variation)
