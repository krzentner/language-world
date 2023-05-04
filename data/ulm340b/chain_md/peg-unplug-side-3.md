
    Steps:  1. Put gripper to the left of the peg  2. Grab the peg with the gripper  3. Slide the peg to the right to get it out of the hole
    The peg is on the right side of the robot, so start by putting the robot's gripper to the left of the peg.
    - When the robot's gripper is not on the left of peg, the robot should put gripper to the left of peg.
    Once the gripper is to the left of the peg, grab the peg.
    - When peg is to the left of the robot's gripper and the peg is not forward aligned with the robot's gripper, the robot should grab peg.
    Now that the robot is holding the peg, slide it to the right to get it out of the hole.
    - When the robot's gripper is left of the peg, the robot should slide peg to the right.

The task `peg-insert-vertical` requires the robot to grab the peg and insert it into the hole from above.
To grab the peg and insert it into the hole from above reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the hole  4. Insert the peg into the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    If the peg is not in front of the gripper, move the gripper above the peg again. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When peg is in front of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    As long the gripper is still mostly around the peg and the peg isn't lined up with the hole, line up the peg with the hole.
    - When the robot's gripper is forward aligned with the peg and the peg is not vertically aligned with hole, the robot should align peg to hole.
    If the peg is lined up with the hole below, insert it.
    - When peg is vertically aligned with hole, the robot should insert peg into hole.

The task `peg-unplug-vertical` requires the robot to grab the peg and pull the it out from above.
To grab the peg and pull the it out from above reliably, the robot should perform the following steps:
    Steps:  1