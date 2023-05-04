

The program has been started for you:

```
# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    if check("the robot's gripper is not above the peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.drop("gripper around peg")
    if check("the robot's gripper is not vertically aligned with the hole and the robot's gripper is not forward aligned with the hole"):
        robot.place("the peg into the hole from the side")
```

Please complete the `peg-insert-side` program by filling in the missing lines of code.  Once your program is correct, you will be able to press Submit.
'''


######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################

from collections import namedtuple
import numpy as np
import random

import itertools
import operator
import pandas as pd
import re

import tensorflow as tf
from tensorflow.keras.optimizers import SGD

from PIL import Image


############################################################################
# TODO: YOUR CODE HERE

class Env(object):
    """
    An environment for the robot to move around in.
    """

    def __init__(self, grid_shape=[3, 3], start=[0, 0], goal=[0, 2], grid_char='#'):
        """
        Input
          - grid_shape: shape of the grid (y, x)
          - start: starting coordinates of robot (y, x)
          - goal: target coordinates of robot (y, x)
          - grid_char: character used for walls in the grid
        """
        self.y, self.x = grid_shape
        self.start = start
        self.goal = goal
        self.grid_char = grid_char
        self.start_grid = [0,0]
        self.goal_grid = [0,0]

        self._build_grid()

        self.grid_char_len = len(self.grid_char)

    def _build_grid(self):
        """
        Build a 2