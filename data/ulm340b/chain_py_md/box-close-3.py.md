

'''

import re
import argparse
import collections
from string import Template

import ipywidgets as widgets
import ipyvuetify as v
import ipyfilechooser

from typing import Union

import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'src'))
import bert_eval

TASKS = {
    'door-open': {
        'steps': [
            "Put gripper above door handle",
            "Drop gripper around door handle",
            "Pull open the door",
        ],
        'code': Template('''# door-open: pull the door open
def door_open(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Pull open the door
    # First, put the gripper mostly above the door handle.
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    # As long as the gripper is still vertically aligned with the door handle,
    # it's being opened, so keep pulling.
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.pull("door open")'''),
        'instructions': "Pull the door open"
    },
    'reach': {
        'steps': [
            "Reach towards the target",
        ],
        'code': Template('''# reach: reach to the target location
def reach(robot):
    # Steps:
    #  1. Reach towards the target
    # We don't have any objects to manipulate, so we can just move the robot's
    # gripper directly to the target location
    if check("the robot's gripper is not near reach target"):
        robot.reach("to goal")'''),
        'instructions': "Reach to the target location"
    },
    'window-close': {