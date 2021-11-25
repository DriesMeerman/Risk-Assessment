import pandas as pd
import matplotlib.pyplot as plt

def _label_mapper_generator(labels, column):
    # return lambda row: labels[row[column]]
    def mapper(row):
        val = row[column]
        if val in labels:
            return labels[val]
        else:
            return val

    return mapper

def dataframe_column_bias(frame: pd.DataFrame, column: str, y_labels=None):
    if y_labels is not None:
        frame[column] = frame.apply(_label_mapper_generator(y_labels, column), axis=1)

    return frame.groupby([column]).size()

def dataframe_column_bias_pie_chart(frame: pd.DataFrame, column: str, y_name=None, y_labels=None):
    y_name = column if y_name is None else y_name
    bias_frame = dataframe_column_bias(frame, column, y_labels)
    bias_frame.plot(kind='pie', y=column, ylabel=y_name, figsize=(8, 8), autopct='%.0f%%')


