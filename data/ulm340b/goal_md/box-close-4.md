

The task `peg-unplug-side` requires the robot to grab the peg and unplug it from the hole from the side.
To grab the peg and unplug it from the hole from the side reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Pull the peg from the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, move the robot's gripper until the robot's gripper is vertically aligned with the peg
    If the peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, move the robot's gripper until the robot's gripper is forward aligned with the peg and the robot's gripper is closed
    If the gripper is mostly around the peg and the peg isn't unhooked, pull the peg out of the hole.
    - When the robot's gripper is forward aligned with the peg, move the robot's gripper until the robot's gripper is above the peg

The task `pick-orient-place` requires the robot to grab the peg, orient it to match the goal and place it on the goal.
To grab the peg, orient it to match the goal and place it on the goal reliably, what steps the robot should perform?

The task `pick-orient-reach-place` requires the robot to grab the peg, orient it to match the goal and place it on the goal by also reaching around an obstacle.
To grab the peg, orient it to match the goal and place it on the goal by also reaching around an obstacle reliably, what steps the robot should perform?

The task `sweep-pile-into-box` requires the robot to sweep all of the blocks into the box.
To sweep all of the blocks into the box reliably, what steps the robot should perform?

The task `pick-heatsink` requires the robot to grab the heatsink with the gripper.
To grab the heatsink with the gripper reliably, what steps the robot should perform?

The task `pick-two-heatsinks` requires the robot to grab both heatsinks with the gripper.
To grab both heatsinks with the gripper reliably, what steps the robot should perform?

The task `pick-block-orient-heatsink-place` requires the robot to grab the heatsink