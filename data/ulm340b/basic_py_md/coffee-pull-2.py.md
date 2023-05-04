

We've provided an image of the initial state [here](https://storage.googleapis.com/robolisp-dataset/tasks/coffee-pull/image_0.png).
There is no time limit for the task, you can run the program many times.


"""

from collections import namedtuple
import random
import os
from glob import glob
import pickle
from typing import List, Tuple

import gym
import gym.spaces
import numpy as np
import imageio
import pygame
from PIL import Image
import ptan

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

import rle

# 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000