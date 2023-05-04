
    Steps:  1. Put gripper above wrench  2. Drop gripper around wrench  3. Pull wrench off peg
    The gripper has to be above the wrench before it can be dropped around it.
    - When the robot's gripper is not above the wrench, the robot should put gripper above wrench.
    Now that the gripper is above the wrench, we can drop it around the wrench.
    - When the robot's gripper is above the wrench and the robot's gripper is open, the robot should drop gripper around wrench.
    If the gripper is around the wrench, we can pull it away from the peg.
    - When the robot's gripper is around the wrench, the robot should pull wrench away from peg.

The task `button-press` requires the robot to press the button from the front.
To press the button from the front reliably, the robot should perform the following steps:
    Steps:  1. Drop the gripper so it is directly above the button  2. Close the gripper so it pushes the button
    We want to push the button from the front, so put the gripper above it.
    - When the robot's gripper is not vertically aligned with button, the robot should place gripper above button.
    When the gripper is above the button, we can close it to push the button.
    - When the robot's gripper is above button, the robot should close gripper to press button.

The task `lever` requires the robot to push the lever down to the right, then to push the lever up to the right.
To push the lever down to the right reliably, the robot should perform the following steps:
    Steps:  1. Put the robot's gripper roughly above the lever handle  2. Start pushing the lever down  3. Push the lever down harder
    The lever handle is large, so we can just put the gripper above it to start.
    - When the robot's gripper is not above lever handle and the robot's gripper is not in front of lever handle, the robot should put gripper above lever handle.
    If the gripper is in front of the lever handle, we can probably push down on the lever.
    - When the robot's gripper is in front of lever handle, the robot should start to push down on lever.
    If the gripper is even more in front of the lever handle, we're pushing harder.
    - When the robot's gripper is far in front of lever handle, the robot should push down on lever harder.

The task `pick-