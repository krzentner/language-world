
Instructions:  Please specify the steps that the robot should perform in the order they should be performed. If you aren't sure, select "I'm not sure".

The task `peg-insert-top` requires the robot to grab the peg and insert it into the hole from the top.
To grab the peg and insert it into the hole from the top reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the hole  4. Insert the peg from above into the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, move the robot's gripper until the robot's gripper is vertically aligned with the peg
    If the peg becomes left of the gripper, go back to putting the gripper above the peg.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, move the robot's gripper until the robot's gripper is forward aligned with the peg and the robot's gripper is closed
    As long the gripper is still mostly around the peg and the peg isn't lined up with the hole, line up the peg with the hole.
    - When peg is horizontally aligned with hole, move the robot's gripper until the robot's gripper is above the peg
    If the peg is lined up with the hole from above, insert it.
    - When the robot's gripper is forward aligned with the peg and the peg is not vertically aligned with hole, move the robot's gripper until the robot's gripper is vertically aligned with hole

The task `peg-unplug-top` requires the robot to grab the peg and pull the it out from the top.
To grab the peg and pull the it out from the top reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the hole  4. Pull the peg out
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, move the robot's gripper until the robot's gripper is vertically aligned with the peg
    If the peg becomes left of the gripper, go back to putting the gripper above the peg.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's grip