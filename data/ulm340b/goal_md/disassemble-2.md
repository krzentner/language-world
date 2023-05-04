
    Steps:  1. Put gripper above wrench  2. Grab wrench with gripper  3. Pull wrench sideways off peg
    First, put the gripper above the wrench.
    - When the robot's gripper is not vertically aligned with the wrench, move the robot's gripper until the robot's gripper is vertically aligned with the wrench
    If the wrench becomes left of the gripper, go back to putting the gripper above the wrench.
    - When the wrench is not left of the robot's gripper and wrench is not forward aligned with the robot's gripper, move the robot's gripper until the robot's gripper is forward aligned with the wrench and the robot's gripper is closed
    As long as the gripper is still mostly around the wrench, we should be able to pull the wrench off the peg by pulling the gripper horizontally to the side.
    - When the robot's gripper is forward aligned with the wrench and the wrench is not horizontally aligned with peg, move the robot's gripper until the robot's gripper is horizontally aligned with peg

The task `peg-insert-side` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into the hole from the side reliably, what steps the robot should perform?
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the hole  4. Slide the peg sideways into the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, move the robot's gripper until the robot's gripper is vertically aligned with the peg
    If the peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, move the robot's gripper until the robot's gripper is forward aligned with the peg and the robot's gripper is closed
    As long the gripper is still mostly around the peg and the peg isn't lined up with the hole, line up the peg with the hole.
    - When peg is horizontally aligned with hole, move the robot's gripper until the robot's gripper is above the peg
    If the peg is lined up with the hole to the side, insert it.
    - When the robot'