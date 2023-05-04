
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Move cube to goal
    # First, put the gripper roughly above cube, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the cube"):
        robot.move_gripper("above the cube")
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.move_gripper("near the cube", close_gripper=True)
    # If the gripper is near the cube and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above the cube and the robot's gripper is closed"):
        robot.move_gripper("left of the target location")
[eod] [code]from .siamese_net import SiameseNet
from .refine_siamese_net import RefineSiameseNet[eod] [code]import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 32})


def f_linear(x):
    y = x
    return y


def f_square(x):
    y = x * x
    return y


def f_sqrt(x):
    y = np.sqrt(x)
    return y


def f_sqrt_log(x):
    y = np.sqrt(np.log(x))
    return y


def f_sin(x):
    y = np.sin(x)
    return y


def f_log(x):
    y = np.log(x)
    return y


x = np.linspace(1, 10, 100)
f1 = f_linear(x)
f2 = f_square(x)
f3 = f_sqrt(x)
f4 = f_sqrt_log(x)
f5 = f_sin(x)
f6 = f_log(x)

plt.figure()
plt.plot(x, f1, "r:", label="$f(x)=