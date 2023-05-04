

"""
        return text
[eod] [code]# coding: utf-8

import os
import pandas as pd
import numpy as np
from itertools import chain

class Dataset(object):
    """ Dataset class"""

    def __init__(self, dir_name, df_name, y_name, label_name, train_ratio=0.8, shuffle_ratio=0.2):
        """
        Creates a Dataset object.

        :param dir_name: A string representing the dir name for the dataset.
        :param df_name: A string representing the df name for the dataset.
        :param y_name: A string representing the y name for the dataset.
        :param label_name: A list of strings representing the label name for the dataset.
        :param train_ratio: The ratio of training dataset.
        :param shuffle_ratio: The ratio of shuffle dataset.
        """
        self.dir_name = dir_name
        self.df_name = df_name
        self.y_name = y_name
        self.label_name = label_name
        self.train_ratio = train_ratio
        self.shuffle_ratio = shuffle_ratio

    def load(self, mode):
        """
        Loads and returns the pandas Dataframe from the dataset directory.

        :param mode: One of ['train', 'val', 'test'].
        :return: pandas Dataframe.
        """
        path = os.path.join(self.dir_name, '%s.csv' % mode)
        df = pd.read_csv(path, index_col=0)
        return df

    def save_as_label(self, df, label_name, label):
        """
        Saves as label.

        :param df: pandas Dataframe.
        :param label_name: Label name.
        :param label: Label value.
        :return: pandas Dataframe.
        """
        df[label_name] = label
        return df

    def split_train_val_test(self, df, split_ratio):
        """
        Splits train, val and test dataframes.

        :param df: pandas Dataframe.
        :param split_ratio: Ratio of train, val and test.
        :return: pandas Dataframe.
        """
        train = df.sample(frac=self.train_ratio)
        val = df[~df.index.isin(train.index)].sample(frac=split_