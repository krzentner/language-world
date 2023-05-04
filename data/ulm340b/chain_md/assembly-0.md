
    Steps:  1. Put gripper above wrench handle  2. Grab the wrench with the gripper  3. Line the wrench up with the peg  4. Move the wrench around the peg until it's attached
    Put gripper above wrench handle
    - When the robot's gripper is not vertically aligned with wrench handle, the robot should put gripper above wrench handle.
    Grab the wrench with the gripper
    - When wrench is not left of the robot's gripper and wrench is not forward aligned with the robot's gripper, the robot should grab wrench.
    Line the wrench up with the peg
    - When the robot's gripper is forward aligned with the wrench and wrench is not vertically aligned with peg, the robot should align wrench to peg.
    Move the wrench around the peg until it's attached
    - When wrench is vertically aligned with peg, the robot should attach wrench around peg.

The task `relocate` requires the robot to grab the box and pull it to the target location.
To grab the box and pull it to the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the box  2. Grab the box with the gripper  3. Move the box to the goal
    Put gripper above the box
    - When the robot's gripper is not vertically aligned with box, the robot should put gripper above box.
    Grab the box with the gripper
    - When box is not left of the robot's gripper and box is not forward aligned with the robot's gripper, the robot should grab box.
    Move the box to the goal
    - When the robot's gripper is forward aligned with the box and box is not near the goal, the robot should move box to goal.

The task `pick-place-v2` requires the robot to pick up the puck and move it to the target location.
To pick up the puck and move it to the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above puck  2. Close the gripper to grab the puck  3. Move the puck to the target location  4. Open the gripper to drop the puck
    If the gripper isn't vertically aligned with the puck, put it above the puck.
    - When the robot's gripper is not above the puck, the robot should place gripper above puck.
    Put the gripper around the puck and close the gripper.
    - When the robot's gripper is above puck and the robot's gripper is open, the robot