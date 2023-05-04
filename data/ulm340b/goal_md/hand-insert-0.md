
    Steps:  1. Put gripper above the puck  2. Drop gripper around the puck  3. Close gripper around puck  4. Move puck to goal
    First, put the gripper roughly above puck, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above puck, move the robot's gripper until the robot's gripper is above puck
    If the gripper isn't around the puck, put it around the puck.
    - When the robot's gripper is not around puck and the robot's gripper is open, move the robot's gripper until the robot's gripper is near the puck and the robot's gripper is closed
    If the gripper is near the puck and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is above puck and the robot's gripper is closed, move the robot's gripper until the robot's gripper is near the target location

The task `sweep` requires the robot to push the box across the table.
To push the box across the table reliably, the robot should perform the following steps:
    Steps:  1. Put gripper to the side of the box  2. Push the box across the table
    If the robot's gripper is forward aligned with the box, we should move the robot's gripper to the side of the box to push it.
    - When the robot's gripper is forward aligned with the box and the box is not near the robot's gripper, move the robot's gripper until the robot's gripper is vertically aligned with the box
    If the gripper is vertically aligned with the box, just start sliding it across the table.
    - When the robot's gripper is not forward aligned with the box, move the robot's gripper until the robot's gripper is near the box
"""
[eod] [code]#!/usr/bin/python3


from setuptools import find_packages, setup

setup(
    name='test-package-pypi',
    version='0.0.1',
    url='http://github.com/dmpayton/test-package-pypi',
    license='MIT',
    author='dmpayton',
    author_email='dmpayton@gmail.com',
    description='A simple Python example package',
    packages=find_packages(exclude=('tests',)),
    install_requires=[],
)
[eod] [code]import numpy as