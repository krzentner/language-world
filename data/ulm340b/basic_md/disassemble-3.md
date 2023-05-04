
"""
            ),
            tutorial_2: """
            Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.

The task `peg-unstack-side` requires the robot to pull a peg from the top of a stack.
To pull a peg from the top of a stack reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with peg and the robot's gripper is above the top of the stack, the robot should put gripper above the top of the stack.
    - When the robot's gripper is vertically aligned with peg, the robot should drop gripper around top of the stack.
    - When the robot's gripper is around the top of the stack, the robot should pull peg from the top of the stack.

The task `reach` requires the robot to reach to the target location.
To reach to the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not near reach target, the robot should reach to goal.

The task `push` requires the robot to slide the puck to the target location.
To slide the puck to the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, the robot should put the gripper above the puck.
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck, the robot should push the gripper into the puck.
    - When the robot's gripper is near the puck and the puck is below the robot's gripper, the robot should slide the puck to the goal.

The task `button-press-topdown` requires the robot to push the button down from above.
To push the button down from above reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.
    - When the robot's gripper is vertically aligned with button, the robot should push down on button.

The task `window-close` requires the robot to slide the window closed to the right.
To slide the window closed to the right reliably, the robot should perform the following steps:
    - When the window handle is right of the robot's gripper and the robot's gripper is not near the window handle, the robot should move gripper to left of window handle.
    - When the robot's gripper is near the window handle, the robot should slide window right.
