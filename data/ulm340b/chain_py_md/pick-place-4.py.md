
"""
[eod] [code]# coding=utf8

import numpy as np
import matplotlib.pyplot as plt

def loadDataSet():
    """
    数据集由四部分组成:
    1. x-coordinate of a point, x-坐标
    2. y-coordinate of the point, y-坐标
    3. label, 1 -> blue dots, 2 -> red dots
    4. cluster of the point, 0 or 1 (0=cluster1,1=cluster2), 聚类结果
    :return: points, 数据点的坐标和标签
    """
    points = [[1, 1, 1, 0], [1, 2, 1, 0], [1, 3, 1, 0], [1, 4, 1, 0], [1, 5, 1, 0],
              [4, 1, 1, 0], [4, 2, 1, 0], [4, 3, 1, 0], [4, 4, 1, 0], [4, 5, 1, 0],
              [2, 3, 1, 0], [2, 4, 1, 0], [2, 5, 1, 0],
              [3, 1, 1, 0], [3, 2, 1, 0], [3, 3, 1, 0], [3, 4, 1, 0], [3, 5, 1, 0],
              [7, 1, 2, 1], [7, 2, 2, 1], [7, 3, 2, 1], [7, 4, 2, 1], [7, 5, 2, 1],
              [6, 4, 2, 1], [6, 3, 2, 1], [6, 5, 2, 1],
              [8, 1, 2, 1], [8, 2, 2, 1], [8, 3, 2, 1], [8, 4, 2, 1], [8, 5, 2, 1],
              [8, 6, 2, 1], [8, 7, 2, 1]]
    return points

def k_means_cluster(points, k):
    """
    k-means聚类,
    :param points: 数据集
    :param