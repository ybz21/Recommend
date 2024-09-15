import numpy as np
import pandas as pd


def process_time_features(df):
    # df['actionTime'] = pd.to_datetime(df['actionTime'])
    # df['publishTime'] = pd.to_datetime(df['publishTime'])
    # df['action_hour'] = df['actionTime'].dt.hour
    # df['action_weekday'] = df['actionTime'].dt.weekday
    df['publish_hour'] = df['publishTime'].dt.hour
    df['publish_weekday'] = df['publishTime'].dt.weekday
    return df.drop(['actionTime', 'publishTime'], axis=1)


def create_cross_features(df, cross_features):
    for name, cols in cross_features:
        df[name] = df[cols[0]] + '_' + df[cols[1]]
    return df.drop('age', axis=1)


# 定义年龄分桶函数
def bin_age(df):
    bins = [0, 18, 30, 45, 60, np.inf]
    labels = ['0-17', '18-29', '30-44', '45-59', '60+']
    df['age_bin'] = pd.cut(df['age'], bins=bins, labels=labels, include_lowest=True)
    # return df.drop('age', axis=1)
    return df
