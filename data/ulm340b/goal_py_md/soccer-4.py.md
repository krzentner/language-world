

The task is for the robot to push a soccer ball into a goal.
For this task, the robot needs to hit the soccer ball to move it
forward, not push it sideways like the puck.
(The soccer ball is too heavy to slide with the gripper.)
The code that you will write will take 3 or 4 steps:

1. `put the gripper above the ball`
1. `push the ball towards the target location`
1. `drop the gripper near the target location`
1. `close the gripper when the target location is reached`

The first step is the same as for the other tasks that involve objects.
After putting the gripper above the ball, push the ball forward by closing
the gripper and moving the robot's gripper forwards.
The soccer ball will only move forwards if the robot's gripper is behind the
soccer ball when it closes.
The robot should open the gripper, drop the gripper near the target location
and close it when the ball gets close to the target.

Once you've written the function and made sure your program runs without
any errors, click the button below to see if it works.
"""
[eod] [code]import torch
import torch.nn as nn
import torch.nn.functional as F


def _make_divisible(v, divisor, min_value=None):
    """
    This function is taken from the original tf repo.
    It ensures that all layers have a channel number that is divisible by 8
    It can be seen here:
    https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/mobilenet.py
    :param v:
    :param divisor:
    :param min_value:
    :return:
    """
    if min_value is None:
        min_value = divisor
    new_v = max(min_value, int(v + divisor / 2) // divisor * divisor)
    # Make sure that round down does not go down by more than 10%.
    if new_v < 0.9 * v:
        new_v += divisor
    return new_v


class h_sigmoid(nn.Module):
    def __init__(self, inplace=True):
        super(h_sigmoid, self).__init__()
        self.relu = nn.ReLU6(inplace=inplace)

    def forward(self, x):
        return self.relu(x + 3) / 6


class h_s