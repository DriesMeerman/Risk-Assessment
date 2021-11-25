import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display
from sklearn.decomposition import PCA, SparsePCA, MiniBatchSparsePCA, FactorAnalysis, FastICA, TruncatedSVD
from sklearn.manifold import TSNE

from helpers import Logger


class DimensionReductionService:

    def __init__(self, logger: Logger):
        self.logger = logger

    def dimension_reduction(self, frame: pd.DataFrame, y_frame: pd.DataFrame, n: int, y_column: str,
                            decomposition_class):
        data = decomposition_class(n_components=n).fit_transform(frame)
        self.logger.info(f"Reduced frame to {n} dimensions")
        display(frame.columns)
        visual_frame = pd.DataFrame(data, columns=['x', 'y'])
        visual_frame[y_column] = y_frame[y_column]
        display(visual_frame)
        return visual_frame

    def show_graph(self, frame: pd.DataFrame, y_column: str, name: str):
        if len(frame.columns) > 3:
            Exception(f"Invalid input dataframe, expecting ['x', 'y', {y_column}]")

        display(frame)
        plt.figure(figsize=(16, 10))
        sns.scatterplot(
            x="x", y="y",
            hue=y_column,
            palette=sns.color_palette("hls"),
            data=frame,
            legend="full",
            alpha=0.3
        )
        # plt.show()
        self.logger.log_img(name)
        plt.close()


    def compare_reducers(self, frame: pd.DataFrame, y_frame: pd.DataFrame, y_column: str, variation_name: str):
        reducers = [PCA, SparsePCA, MiniBatchSparsePCA, FactorAnalysis, FastICA, TruncatedSVD, TSNE]
        self.logger.info("Comparing reducers")
        for reducer in reducers:
            reducer_name = reducer.__name__
            self.logger.info(f"### {reducer_name}")
            reduced_df = self.dimension_reduction(frame, y_frame=y_frame, n=2, y_column=y_column,
                                                  decomposition_class=reducer)
            self.show_graph(reduced_df, y_column, f"dimension_reduced_{variation_name}_{reducer_name}")
