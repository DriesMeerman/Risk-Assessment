
from helpers.logger import Verbosity
import time
from typing import Dict
import pandas as pd
import seaborn as sns

from IPython.display import display
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
import math

from .ModelTest import ModelTest, ConfigHelper


class DTModelTest(ModelTest):
    def __init__(self, training_df: pd.DataFrame, config, variation: str) -> None:
        super().__init__(training_df, config=config, feature_variation=variation)
        self.name = "Decision Tree"
        self.name_short = "DT"
        self.max_depth = {'All': None}
        self.criterion = 'gini'
        self.splitter = 'best'

    def train_model(self):
        self.logger.debug("Start training.")
        start = time.time()
        max_depth = list(self.max_depth.values())[0]
        model = DecisionTreeClassifier(criterion=self.criterion,
                                       splitter=self.splitter,
                                       max_depth=max_depth)
        model.fit(self.X_train, self.y_train)
        fit_time = time.time() - start
        self.logger.debug("Fit model in {} seconds".format(
                            round(fit_time, 2)))
        self.fit_time = fit_time
        self.model = model
        self.calc_accuracy()

    def optimize_config(self):
        # https://towardsdatascience.com/how-to-tune-a-decision-tree-f03721801680
        row_count = self.get_train_row_count()
        depths = {
            'All':  None,
            'Log':  round(math.log(row_count)),
            'Sqrt': round(math.sqrt(row_count)),
            '75%':  round(row_count * 0.75),
            '50%':  round(row_count / 2),
            '25%':  round(row_count / 4),
            '5': 5
        }

        criteria = ['gini', 'entropy']
        splitters = ['best', 'random']

        pd_columns = ['Depth', 'Depth Count', 'Criterion', 'Splitter', 'Accuracy']
        accuracy_frame = pd.DataFrame(columns=pd_columns)

        verbosity = self.logger.verbosity
        self.logger.set_verbosity(Verbosity.warning)
        for c in criteria:
            self.criterion = c
            for s in splitters:
                self.splitter = s
                for key, val in depths.items():
                    self.max_depth = {key: val}
                    self.train_model()

                    row = {
                        'Depth': key,
                        'Depth Count': val,
                        'Criterion': c,
                        'Splitter': s,
                        'Accuracy': self.accuracy
                    }
                    accuracy_frame = accuracy_frame.append(row, ignore_index=True)

        self.logger.set_verbosity(verbosity)

        accuracy_frame = accuracy_frame.sort_values(by=['Accuracy'], ascending=False)
        best = accuracy_frame.head(1).iloc[0]

        self.max_depth = depths[best['Depth']]
        self.criterion = best['Criterion']
        self.splitter = best['Splitter']

        self.best_mean_fit_time = self.fit_time

        self.logger.info("Optimized config with:  \n{}".format(best))
        if self.logger.is_info():
            # display(accuracy_frame)
            self.logger.df(accuracy_frame)

            accuracy_frame['Name'] = accuracy_frame[['Depth', 'Criterion', 'Splitter']].agg('-'.join, axis=1)
            visual = accuracy_frame[['Name', 'Accuracy']]
            cm = sns.light_palette("green", as_cmap=True)
            accuracy_frame.style.background_gradient(cmap=cm)
            fig, ax = plt.subplots(figsize=(8,8))
            sns.set(style="whitegrid")
            sns.barplot(y='Name', x="Accuracy", data=visual, ax=ax)
            # plt.show()
            self.save_plot()

    @staticmethod
    def get_model(frame: pd.DataFrame, config: ConfigHelper, variation: str):
        return DTModelTest(frame, config, variation)
