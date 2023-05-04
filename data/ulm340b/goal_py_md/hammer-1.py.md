

'''
import utils

import gym
import gym_minigrid
import numpy as np
import pybullet_envs
import time
import sys

from gym.spaces import prng, Discrete, MultiDiscrete, Box, Tuple, Dict
from gym.spaces import flatdim, _basestring

gym.logger.set_level(40)

gym_minigrid.register(
    id='MiniGrid-Empty-8x8-v0',
    entry_point=gym_minigrid.envs:empty_env,
    kwargs={'width': 8, 'height': 8},
    max_episode_steps=200,
    reward_threshold=0.0
)

gym_minigrid.register(
    id='MiniGrid-Empty-RedBlueDoors-6x6-v0',
    entry_point=gym_minigrid.envs:empty_env,
    kwargs={
        'width': 6,
        'height': 6,
        'num_rooms': 0,
        'doors_colors': ['red', 'blue'],
        'num_keys': 1
    },
    max_episode_steps=200,
    reward_threshold=0.0
)

env = gym.make('MiniGrid-Empty-8x8-v0')

def button_press_topdown(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button")

def door_open(robot):
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.move_gripper("almost vertically aligned with the door handle", close_gripper=True)
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.move_gripper("left of the door handle")

def reach(robot):
    if check("the robot's gripper is not near reach target"):
        robot.move_gripper("near the reach target")

def drawer_close(robot):
    if check("the robot's gripper is not near the drawer handle"):
        robot.move_gripper("near the drawer handle")
    if check