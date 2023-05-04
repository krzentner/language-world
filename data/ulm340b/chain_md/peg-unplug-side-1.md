:
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Slide the peg out of the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    If the peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    As long the gripper is still mostly around the peg and the peg isn't pulled out yet, pull it out of the hole.
    - When the robot's gripper is forward aligned with the peg and the peg is not pulled out yet, the robot should slide the peg out of the hole.

The task `peg-insert-topdown` requires the robot to grab the peg and insert it into the hole from above.
To grab the peg and insert it into the hole from above reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the hole  4. Slide the peg down into the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    If the peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    As long the gripper is still mostly around the peg and the peg isn't lined up with the hole, line up the peg with the hole.
    - When the robot's gripper is forward aligned with the peg and the peg is not vertically aligned with hole, the robot should align peg to hole.
    If the peg is lined up with the hole from above, insert it.
    - When peg is vertically aligned with hole, the robot should insert peg into hole.

The task `peg-unplug-topdown` requires the robot to grab the peg and pull the it out from above.
To grab the peg and pull the