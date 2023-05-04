
"""

# This is the robot. You can use it to see where things are.
robot = RobotWorld()

# Commands you can give the robot:
def move_gripper(direction, close_gripper=False):
    # direction can be:
    #     above (object),
    #     below (object),
    #     left-of (object),
    #     right-of (object),
    #     near (object)
    #     almost (object)
    #     forward (object),
    #     back (object)
    #     vertically-aligned (object)
    #     horizontally-aligned (object)
    #     unaligned
    pass


def check(statement):
    """Return True if statement is true, and False otherwise."""
    pass


# The tasks you should complete.
# Feel free to copy code between tasks.
def reach(robot):
    """Reach to the target location."""
    pass


def push(robot):
    """Slide the puck to the target location."""
    pass


def pick_place(robot):
    """Pick up the puck and hold it at the target location."""
    pass


# Functions for each task:
def button_press_topdown(robot):
    """Push the button down from above."""
    pass


def drawer_open(robot):
    """Pull the drawer open."""
    pass


def drawer_close(robot):
    """Push the drawer close."""
    pass


def door_open(robot):
    """Pull the door open."""
    pass


def window_close(robot):
    """Slide the window closed to the right."""
    pass


def window_open(robot):
    """Slide the window open to the left."""
    pass


def peg_insert_side(robot):
    """Grab the peg and insert it into the hole from the side."""
    pass


def hand_insert(robot):
    """Pick up the puck and move it to the target location."""
    pass
[eod] [code]#!/usr/bin/env python3

# (C) Copyright 2021 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECM