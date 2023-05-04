
    Steps:  1. Put gripper above button  2. Press the button
    The robot can press the button from above by moving gripper on top of it and pressing down. If the button is not below the gripper as seen from above, move the gripper above the button.
    - When the robot's gripper is not above button and the robot's gripper is not vertically aligned with button, the robot should put gripper above button.
    If the gripper is vertically aligned with the button but not near it, move the gripper down to the button.
    - When the robot's gripper is vertically aligned with button and the robot's gripper is not near button, the robot should press button.

The task `reach` requires the robot to reach to the target location.
To reach to the target location reliably, the robot should perform the following steps:
    Steps:  1. Reach towards the target
    We don't have any objects to manipulate, so we can just move the robot's gripper directly to the target location
    - When the robot's gripper is not near reach target, the robot should reach to goal.

The task `peg-insert-side` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into the hole from the side reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the hole  4. Slide the peg sideways into the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    If the peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    As long the gripper is still mostly around the peg and the peg isn't lined up with the hole, line up the peg with the hole.
    - When the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole, the robot should align peg to hole.
    If the peg is lined up with the hole to the side, insert it.
    - When peg is horizontally aligned with hole, the robot should insert peg into hole.

The