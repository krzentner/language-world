

You must fill in the code between the `def` and `def` statements, including what conditional statements and actions to write,
in a way that causes the robot to complete the task of sliding a plate into a target location.
"""

###############################################################
# put the robot's gripper above the plate.

def plate_slide(robot):
    """slide the plate into the target location"""
    if check("the robot's gripper is not above the plate"):
        robot.place("gripper above plate")

###############################################################
# drop the robot's gripper onto the plate.

def plate_slide(robot):
    """slide the plate into the target location"""
    if check("the robot's gripper is not above the plate"):
        robot.place("gripper above plate")
    if check("the robot's gripper is above the plate"):
        robot.drop("gripper onto plate")

###############################################################
# close the robot's gripper around the plate.

def plate_slide(robot):
    """slide the plate into the target location"""
    if check("the robot's gripper is not above the plate"):
        robot.place("gripper above plate")
    if check("the robot's gripper is above the plate"):
        robot.drop("gripper onto plate")
    if check("the robot's gripper is around the plate and the robot's gripper is open"):
        robot.close("gripper around plate")

###############################################################
# push the plate toward the target location.

def plate_slide(robot):
    """slide the plate into the target location"""
    if check("the robot's gripper is not above the plate"):
        robot.place("gripper above plate")
    if check("the robot's gripper is above the plate"):
        robot.drop("gripper onto plate")
    if check("the robot's gripper is around the plate and the robot's gripper is open"):
        robot.close("gripper around plate")
    if check("the robot's gripper is around the plate"):
        robot.push("the plate to the goal")
[eod] [code]# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 18:55:02 2020

@author: michael
"""


import math, itertools, functools
import numpy as