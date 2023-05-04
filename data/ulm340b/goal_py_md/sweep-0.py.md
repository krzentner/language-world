

The function you write should take as its only argument the robot, and
perform the `sweep` task. You can call the `robot.move_gripper` method to
control the robot. You can also check whether certain facts are true about
the robot's current state by calling the `check` function, as described in
the code.

"""

# sweep: grab the cube and move sideways it to the target location
def sweep(robot):
    """
    This function controls the robot to sweep the cube from the start location to the goal.
    :param robot: robot object to control
    :return: None
    """
    # Steps:
    #  1. Put gripper above cube
    #  2. Grab cube with gripper
    #  3. Slide gripper sideways with cube to target location
    # If the gripper is above the cube, grab the cube with the gripper.
    if check("the robot's gripper is above the cube"):
        robot.move_gripper("almost vertically aligned with the cube")
    # If the cube is between the left and right edges of the gripper, we can probably grab it.
    # Move the gripper down to grab the cube.
    if check("the robot's gripper is left of the cube and the robot's gripper is not right of the cube"):
        robot.move_gripper("near the cube", close_gripper=True)
    # Now that the robot's gripper is closed around the cube, we can move the cube by moving the gripper.
    # Slide the cube along the table to the target location.
    if check("the robot's gripper is above the cube and the cube is between the left and right edges of the robot's gripper"):
        robot.move_gripper("vertically aligned with the target location")
    return None

def main():
    print(sweep.__doc__)

if __name__ == "__main__":
    main()
[eod] [code]from ._ssim import ssim, msssim
from ._ssim import __version__


__all__ = [ssim, msssim]
[eod] [code]import tensorflow as tf
import numpy as np

from tensorflow.python.ops.rnn_cell_impl import _linear


class Model(object):
    """The Sequence-to-sequence model."""

    def __init__(self, config, source_vocab_size, target_vocab_size,