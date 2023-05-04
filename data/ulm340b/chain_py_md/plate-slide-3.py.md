

Once you have a working solution, press the red button.

You can use the functions `check_button_press()` to check the gripper against the button,
`check_drawer_open()` to check the gripper against the drawer, `check_door_open()` to check
the gripper against the door, `check_drawer_close()` to check the gripper against the drawer
handle, `check_window_open()` to check the gripper against the window handle, `check_window_close()`
to check the gripper against the window handle, `check_peg_insert_side()` to check the gripper
against the peg, `check_pick_place()` to check the gripper against the puck,
`check_reach()` to check the gripper against the goal location, `check_push()` to check the gripper
against the puck, and `check_plate_slide()` to check the gripper against the plate
to help you write your program.
If the gripper is in the right position, the function will return `True`,
otherwise it will return `False`.
"""


# Steps:
#  1. Put gripper at edge of plate
#  2. Slide plate sideways into goal
# Because this is sideways, we can just move the gripper to the edge of the plate.

if check("the robot's gripper is not next to the plate and the robot's gripper is above the plate"):
    robot.move("the gripper to the edge of the plate")

# Once the gripper is at the edge of the plate, we can slide it to the goal.

if check("the robot's gripper is next to the plate and the robot's gripper is above the plate"):
    robot.slide("the plate to the goal")
[eod] [code]#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup, find_packages

version = '0.1.0'

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

install_requires = [
    'requests',
    'jinja2',
]

test_requires = [
    'pytest',
    'pytest-httpbin',
    'httpbin',
    'codecov',
    'pytest-cov',
]

docs_requires = [
    'sphinx',
