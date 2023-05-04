

```
# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):
    if check("robot gripper is not left of mug"):
        robot.place("gripper to the left of the mug")
    if check("robot gripper is not around mug"):
        robot.align("gripper with the mug")
    if check("robot gripper is not near mug"):
        robot.pull("mug")
    if check("robot gripper is around mug"):
        robot.align("robot gripper towards goal")
    if check("robot gripper is near goal"):
        robot.drop("gripper around mug")
    if check("robot gripper is in front of goal"):
        robot.place("gripper towards goal")


print(coffee_push(robot))
```[eod] [code]# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.model_selection import train_test_split
import torch
from torch.autograd import Variable
from torch.nn import functional as F
from torch.utils.data import Dataset, DataLoader
import os
import torch.nn as nn
import numpy as np
from sklearn.metrics import accuracy_score

def split_train_eval(train, train_per=0.6):
    """Split train data to train and eval data.
    Args:
        train: pandas.DataFrame
            raw data
        train_per: float
            data percentage for training. 0.2 for 20%
    Return:
        train_df, eval_df: pandas.DataFrame
    """
    num_total = train.shape[0]
    num_train = int(train_per * num_total)
    eval_idx = num_train + np.random.permutation(num_total-num_train)[:num_total-num_train]
    train_idx = np.setdiff1d(np.arange(num_total), eval_idx)
    train_df = train.iloc[train_idx]
    eval_df = train.iloc[eval_idx]
    return train_df, eval_df


def split_train_valid_eval(train, valid_per=0.1, eval_per=0.3):
    """Split train data to train, valid and eval data.
    Args:
        train: pandas.DataFrame
            raw data
        valid_