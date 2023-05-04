
"""
[eod] [code]from math import *
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sciop
import time
import yaml
import sys
import os


def plot_2d_slice_1st_plane(plane_pos, data):

    plane_num = 0
    N = len(data)

    x, y, z = zip(*data[:, 0:3])
    data = np.array(data).astype(float)

    f, ax = plt.subplots(figsize=(6, 5))
    c = ax.contourf(x, y, data[:, plane_num])
    cbar = f.colorbar(c)

    ax.scatter(data[plane_pos, 0], data[plane_pos, 1], c='r')
    cbar.set_label('$\eta / \pi$')
    ax.grid()
    plt.show()


def plot_2d_slice_2nd_plane(plane_pos, data):

    plane_num = 1
    N = len(data)

    x, y, z = zip(*data[:, 0:3])
    data = np.array(data).astype(float)

    f, ax = plt.subplots(figsize=(6, 5))
    c = ax.contourf(x, y, data[:, plane_num])
    cbar = f.colorbar(c)

    ax.scatter(data[plane_pos, 0], data[plane_pos, 1], c='r')
    cbar.set_label('$\phi / \pi$')
    ax.grid()
    plt.show()


def plot_2d_slice_3rd_plane(plane_pos, data):

    plane_num = 2
    N = len(data)

    x, y, z = zip(*data[:, 0:3])
    data = np.array(data).astype(float)

    f, ax = plt.subplots(figsize=(6, 5))
    c = ax.contourf(x, y, data[:, plane_num])
    