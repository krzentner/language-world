
    Steps:  1. Put gripper above the handle  2. Drop gripper around the handle  3. Pull the handle up
    Because the robot's gripper is at an angle and the handle is a long object, we need to put the gripper above the handle.
    - When the robot's gripper is not vertically aligned with handle, move the robot's gripper until the robot's gripper is vertically aligned with handle
    We need to make sure the gripper is around the handle before pulling it up.
    - When the robot's gripper is vertically aligned with handle and the robot's gripper is not forward aligned with handle, move the robot's gripper until the robot's gripper is forward aligned with handle
    When the gripper is lined up with the handle as viewed from the front and the gripper is closed, maybe we can pull up the handle.
    - When the robot's gripper is forward aligned with handle and the robot's gripper is closed, move the robot's gripper until the robot's gripper is near the handle

The task `handle-pull-topdown` requires the robot to pull up the handle by pushing down on the gripper.
To pull up the handle by pushing down on the gripper reliably, what steps the robot should perform?
    Steps:  1. Put the gripper above the handle  2. Lower the gripper around the handle  3. Push the handle up
    Because the robot's gripper is at an angle and the handle is a long object, we need to put the gripper above the handle.
    - When the robot's gripper is not vertically aligned with handle, move the robot's gripper until the robot's gripper is vertically aligned with handle
    We need to make sure the gripper is around the handle before pushing the gripper to pull the handle up.
    - When the robot's gripper is vertically aligned with handle and the robot's gripper is not forward aligned with handle, move the robot's gripper until the robot's gripper is forward aligned with handle
    When the gripper is lined up with the handle as viewed from the front, maybe we can push up the handle by lowering the gripper.
    - When the robot's gripper is forward aligned with handle, move the robot's gripper until the robot's gripper is above the handle
"""
import copy
import itertools
import json
import pickle
import pprint
import os
import sys

import utils
import rl_sandbox.constants as c

import numpy as np

import rl_sandbox.aux