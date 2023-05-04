
    Steps:  1. Put gripper above drawer handle  2. Put gripper below drawer handle  3. Close drawer
    First, put the gripper above the drawer handle.
    - When the robot's gripper is not above drawer handle, move the robot's gripper until the robot's gripper is above drawer handle
    If the gripper is above drawer handle we should be able to put it down around the drawer handle.
    - When the robot's gripper is above drawer handle, move the robot's gripper until the robot's gripper is below drawer handle
    If the gripper is below the drawer handle we can probably close the drawer.
    - When the robot's gripper is below drawer handle, move the robot's gripper until the robot's gripper is horizontally aligned with the drawer handle

The task `button-press-side` requires the robot to push the button from the side.
To push the button from the side reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper as viewed from the side  2. Push the button forward
    Because this is "side", we just need to line up the gripper from the side. Put the gripper in front of the button.
    - When the robot's gripper is in front of the button, move the robot's gripper until the robot's gripper is forward aligned with the button
    Now that the gripper is lined up, just push the button forward.
    - When the robot's gripper is horizontally aligned with button, move the robot's gripper until the robot's gripper is in front of the button

The task `drawer-close-v2` requires the robot to push the drawer close.
To push the drawer close reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above drawer handle  2. Drop gripper around drawer handle  3. Push drawer closed
    First, put the gripper roughly above the drawer handle.
    - When the robot's gripper is not vertically aligned with drawer handle, move the robot's gripper until the robot's gripper is vertically aligned with the drawer handle
    If the gripper is aligned with the drawer handle we should be able to drop it around the drawer handle.
    - When the robot's gripper is vertically aligned with the drawer handle and the robot's gripper is not around the drawer handle, move the robot's gripper until the robot's gripper is around the drawer handle
    If the gripper is around the drawer handle, we can push