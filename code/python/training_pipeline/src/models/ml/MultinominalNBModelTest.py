
import time
import pandas as pd
from sklearn.naive_bayes import MultinomialNB

from .ModelTest import ModelTest, ConfigHelper


class MultinominalNBModelTest(ModelTest):
    def __init__(self, training_df: pd.DataFrame, config, variation: str) -> None:
        super().__init__(training_df, config=config, feature_variation=variation)
        self.name = "Multinominal Naive Bayes"
        self.name_short = "MNB"

    def train_model(self):
        self.logger.debug("Start training.")
        start = time.time()
        model = MultinomialNB()
        model.fit(self.X_train, self.y_train)
        fit_time = time.time() - start
        self.best_mean_fit_time = fit_time
        self.logger.debug("Fit model in {} seconds".format(round(fit_time, 2)))
        self.model = model
        self.calc_accuracy()

    def optimize_config(self):
        self.logger.debug("NB does not have hyperparams to tune")
        self.train_model()

    @staticmethod
    def get_model(frame: pd.DataFrame, config: ConfigHelper, variation: str):
        return MultinominalNBModelTest(frame, config, variation)


