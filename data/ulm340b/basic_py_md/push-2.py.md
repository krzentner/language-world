

Then write your solution below the provided code.
"""

# push: slide the puck to the target location
def push(robot):
    if check("the robot's gripper is not around the puck and the robot's gripper is not left of the puck"):
        robot.place("gripper to left of puck")
    if check("the robot's gripper is not around puck"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is around puck and the puck is not on the target location"):
        robot.slide("puck on target")
"""

# Test 3
def _test_3(test, msg):
    if len(test) == 0:
        return msg("Test did not compile.")

    try:
        test = list(test.values())
    except (AttributeError, TypeError):
        test = [test]

    try:
        test = next(test)
    except (AttributeError, StopIteration):
        return msg("Test did not compile.")

    try:
        test = next(test.values())
    except (AttributeError, StopIteration):
        return msg("Test did not compile.")

    import ast

    test_funcs = [
        x.name for x in ast.walk(ast.parse(test)) if isinstance(x, ast.FunctionDef)
    ]

    if "reach" in test_funcs:
        return msg(None)

    return msg("""
# push: slide the puck to the target location
def push(robot):
    if check("the robot's gripper is not around the puck and the robot's gripper is not left of the puck"):
        robot.place("gripper to left of puck")
    if check("the robot's gripper is not around puck"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is around puck and the puck is not on the target location"):
        robot.slide("puck on target")

""")
[eod] [code]# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 12:53:41 2016

@author: sroy
"""


import numpy as np
import glob, gzip


def load_data_wrapper(dataset, preproc=None, train_frac=0.9, val_frac