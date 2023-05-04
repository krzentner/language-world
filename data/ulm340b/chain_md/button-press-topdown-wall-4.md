
    Just like `button-press-topdown`, except we need to line up the robot's gripper both from above and from the front.
    Steps:  1. Line up the gripper from above and from the front  2. Push down on the button from the top

The task `drawer-close-side` requires the robot to push the drawer closed from the side.
To push the drawer closed from the side reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper in front of the drawer handle  2. Push the drawer closed
    We can push the drawer closed as long as the gripper is in front of the drawer handle.
    - When the robot's gripper is not forward aligned with drawer handle, the robot should grab drawer handle.
    If the gripper is aligned with the drawer handle as seen from in front, push the drawer closed.
    - When the robot's gripper is forward aligned with drawer handle, the robot should push drawer closed.

The task `button-press-side` requires the robot to press the button from the side.
To press the button from the side reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper with the button from the front  2. Push the button from the side
    First, line up the gripper as seen from in front.
    - When the robot's gripper is not horizontally aligned with button, the robot should line up gripper with button.
    Once the gripper is lined up, push the button sideways.
    - When the robot's gripper is horizontally aligned with button, the robot should press button.

The task `door-open-side` requires the robot to pull the door open from the side.
To pull the door open from the side reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper with the door handle from the front  2. Pull the door open
    First, line up the gripper with the door handle as seen from in front.
    - When the robot's gripper is not horizontally aligned with door handle, the robot should put gripper around door handle.
    Once the gripper is lined up, we can just pull the door open.
    - When the robot's gripper is horizontally aligned with door handle, the robot should pull door open.

The task `peg-unstack` requires the robot to pull the peg up out of the hole.
To pull the peg up out of the hole reliably, the robot should perform the following steps:
    Steps:  1. Put the