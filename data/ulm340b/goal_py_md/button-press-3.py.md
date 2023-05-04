

## Input: ##

You will have access to the following functions that you should use to write
your program:

* **check(string)**: Returns `True` if the state of the world matches the given
    string. Returns `False` otherwise.
* **move_gripper(string, close_gripper=False)**: You can control the
    robot's arm through this function.
    This function takes in two arguments:

    * The first argument is a string describing the desired position of
      the gripper, such as `"near the reach target"`.
    * The second argument indicates whether you want to close the
      gripper in the next step, or leave it open.
      Possible values are `True` for close, and `False` for leave it open.

## Output: ##

You should write a function named `button_press` that accepts a single argument
"robot", which is an object containing helper functions for moving the robot's
arm. Your function should use these helper functions to move the robot's gripper
to the desired position as instructed. Your function should not return any
values.

## Scoring: ##

You will be scored based on how well your program performs the task.
"""


def check(string):
    return True  # Check your state. Returns true if state matches string.


# Gripper-based API:


def move_gripper(string, close_gripper=False):
    print("Move gripper to " + string + ".")
    print("Close gripper " + str(close_gripper).lower())


# Reach:
def reach(robot):
    # Steps:
    #  1. Reach towards the target
    # We don't have any objects to manipulate, so we can just move the robot's
    # gripper directly to the target location
    if check("the robot's gripper is not near reach target"):
        robot.move_gripper("near the reach target")


# Peg-insert-side:
def peg_insert_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg sideways into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.