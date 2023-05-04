

Then fill in lines of code, similar to the ones above. There should be 3.
The first and second one should both use `check()` to test conditions and `robot.*()` to perform actions.
The last one should only use `robot.*()` to perform actions.

You should only need to use conditions from `conditions_all`, but you can use any actions from `actions_all`.

## How to complete this lesson

The lesson is complete when your `pick_out_of_hole()` program causes the robot to `put the peg above the goal`, `move the gripper below the peg`, and then `place the peg at the goal`.

"""


# Conditions
conditions_all = [
    # robot's gripper is not vertically aligned with button
    "robot's gripper is not vertically aligned with button",

    # robot's gripper is vertically aligned with button
    "robot's gripper is vertically aligned with button",

    # robot's gripper is not almost vertically aligned with door handle
    "robot's gripper is not almost vertically aligned with door handle",

    # robot's gripper is almost vertically aligned with the door handle
    "robot's gripper is almost vertically aligned with the door handle",

    # robot's gripper is vertically aligned with door handle
    "robot's gripper is vertically aligned with door handle",

    # robot's gripper is above the robot's gripper is not around drawer handle
    "robot's gripper is above the robot's gripper is not around drawer handle",

    # robot's gripper is not around drawer handle
    "robot's gripper is not around drawer handle",

    # robot's gripper is around drawer handle
    "robot's gripper is around drawer handle",

    # the robot's gripper is not near the drawer handle
    "the robot's gripper is not near the drawer handle",

    # robot's gripper is near the drawer handle
    "robot's gripper is near the drawer handle",

    # the robot's gripper is forward aligned with drawer handle
    "the robot's gripper is forward aligned with drawer handle",

    # window handle is right of the robot's gripper and the robot's gripper is not near the window handle
    "window handle is right of the robot's gripper and the robot's gripper is not near the window handle",

    # the robot's gripper is