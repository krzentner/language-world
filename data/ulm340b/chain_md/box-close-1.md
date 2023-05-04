
    Steps:  1. Put gripper above box lid  2. Drop gripper around box lid  3. Close gripper around box lid  4. Move box lid to box  5. Drop box lid onto box
    First, put the gripper roughly above box lid, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above box lid, the robot should place gripper above box lid.
    If the gripper isn't around box lid, put it around box lid.
    - When the robot's gripper is not around box lid and the robot's gripper is open, the robot should drop gripper around box lid.
    If the gripper is near box lid and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is near box lid and the robot's gripper is open, the robot should close gripper around box lid.
    We closed the gripper, and box lid is still near the gripper, so maybe we grabbed it. Try to move box lid to the box. If we didn't grab it, we'll just go back to an earlier step.
    - When the robot's gripper is above box lid and the robot's gripper is closed, the robot should move box lid to box.
    If box lid is above box, we can put it down.
    - When box lid is above box, the robot should drop box lid onto box.

The task `peg-unstack` requires the robot to grab the top peg and move it away from the bottom peg.
To grab the top peg and move it away from the bottom peg reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above top peg  2. Grab the top peg with the gripper  3. Move the top peg away from the bottom peg
    First, put the gripper above the top peg.
    - When the robot's gripper is not vertically aligned with top peg, the robot should put gripper above top peg.
    If the top peg is left of the gripper, go back to putting the gripper above the top peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When top peg is not left of the robot's gripper and top peg is not forward aligned with the robot's gripper, the robot should grab top peg.
    As long the top peg is still mostly around the gripper, we can move the top peg away.
    - When top