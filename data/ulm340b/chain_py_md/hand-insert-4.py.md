
"""


def hand_insert(robot):
    # Steps:
    #  1. Move the gripper above the puck
    #  2. Put the puck in the gripper by moving the gripper down until it's
    #    below the puck
    #  3. Move the gripper to the goal
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # We closed the gripper, and the puck is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the puck to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")


def check(description):
    return 1


robot = {
    "place": print,
    "move": print,
    "drop": print,
    "put": print,
    "grab": print,
    "close": print,
    "reach": print,
    "slide": print,
    "push": print,
    "pull": print,
    "insert": print,
    "align": print
}

hand_insert(robot)
[eod] [code]import numpy as np
from pandas import Series, DataFrame
import pandas as pd

from sklearn import preprocessing, tree, metrics

from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn import linear_model

from sklearn import svm
import pandas as pd
import numpy as np



class LearningModel(object):
