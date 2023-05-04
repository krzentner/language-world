

The task `scoop` requires the robot to pick up the puck from the floor and hold it at the target location.
To pick up the puck from the floor and hold it at the target location reliably, what steps the robot should perform?

The task `window-close-side` requires the robot to push the window to the right to close it, from the side.
To push the window to the right to close it, from the side reliably, what steps the robot should perform?

The task `window-open-side` requires the robot to push the window to the left to open it, from the side.
To push the window to the left to open it, from the side reliably, what steps the robot should perform?

The task `button-press` requires the robot to push the button down.
To push the button down reliably, what steps the robot should perform?

"""

_INSTRUCTIONS_TRAIN_A = """
Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.


The task `door-open` requires the robot to pull the door open.
To pull the door open reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above door handle  2. Drop gripper around door handle  3. Pull open the door
    First, put the gripper mostly above the door handle.
    - When the robot's gripper is not almost vertically aligned with door handle, the robot should put gripper above door handle.
    As long as the gripper is almost lined up, closing it should line it up all the way.
    - When the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open, the robot should put gripper around door handle.
    As long as the gripper is still vertically aligned with the door handle, it's being opened, so keep pulling.
    - When the robot's gripper is vertically aligned with the door handle, the robot should pull door open.


The task `button-press-topdown` requires the robot to push the button down from above.
To push the button down from above reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper as viewed from above  2. Push down on the button from the top
    Because this is "topdown", we just need to line up the gripper from above. Line up the robot's gripper from above.
    - When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.
    Now