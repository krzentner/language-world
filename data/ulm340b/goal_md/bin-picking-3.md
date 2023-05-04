
    Steps:  1. Put gripper above bin  2. Pick up the cube  3. Move the cube to the target bin
    Since we need to move the cube out of the bin and then back into it, first put the gripper above the bin.
    - When the robot's gripper is not above bin, move the robot's gripper until the robot's gripper is above bin
    We can just lift the cube out of the bin because the cube is small enough.
    - When the robot's gripper is not vertically aligned with cube and the robot's gripper is closed, move the robot's gripper until the robot's gripper is vertically aligned with cube
    If the gripper is below the bin, we can put the cube back in by moving the robot's gripper to the target bin.
    - When the robot's gripper is not below bin and the robot's gripper is closed, move the robot's gripper until the robot's gripper is below bin

The task `pick-out-of-hole` requires the robot to pick the peg out of the hole.
To pick the peg out of the hole reliably, the robot should perform the following steps:
    Steps:  1. Line the gripper up with the peg  2. Put the gripper above the peg  3. Pull the peg out of the hole
    If the robot's gripper is not vertically aligned with the peg, line up the gripper with the peg.
    - When the robot's gripper is not vertically aligned with peg and the robot's gripper is open, move the robot's gripper until the robot's gripper is vertically aligned with peg
    If the robot's gripper is not above the peg, move the gripper above the peg.
    - When the robot's gripper is not above peg and the robot's gripper is vertically aligned with peg, move the robot's gripper until the robot's gripper is above the peg
    If the robot's gripper is above the peg, we should pull the peg out.
    - When the robot's gripper is not above the peg and the robot's gripper is closed, move the robot's gripper until the robot's gripper is vertically aligned with peg

The task `stack` requires the robot to pick up the puck and hold it above the other puck.
To pick up the puck and hold it above the other puck reliably, what steps the robot should perform?
    Steps:  1. Put gripper above puck  2. Drop gripper around puck  3. Close gripper