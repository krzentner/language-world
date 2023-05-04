
    Steps:  1. Put gripper above ball  2. Drop gripper around ball  3. Close gripper around ball  4. Move puck to goal
    - When the robot's gripper is not around basketball, move the robot's gripper until the robot's gripper is around basketball
    - When the robot's gripper is near the goal, move the robot's gripper until the robot's gripper is not near the goal
    - When the robot's gripper is near basketball, move the robot's gripper until the robot's gripper is not near basketball
    - When the robot's gripper is around basketball, move the robot's gripper until the robot's gripper is above the goal

The task `peg-unstack` requires the robot to unstack a peg from the pile of pegs.
To unstack a peg from the pile of pegs reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the top of the pile of pegs  2. Close gripper around the top peg  3. Pull up with gripper to unstack the top peg
    First, put the gripper above the top of the pile of pegs.
    - When the robot's gripper is not vertically aligned with the top of the pile of pegs, move the robot's gripper until the robot's gripper is vertically aligned with the top of the pile of pegs
    If the gripper isn't around the peg, put it around the peg.
    - When the robot's gripper is vertically aligned with the top of the pile of pegs and the robot's gripper is not around peg, move the robot's gripper until the robot's gripper is around peg
    If the gripper is near the peg and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is around the top of the pile of pegs, move the robot's gripper until the robot's gripper is below peg

The task `block-pickup` requires the robot to pick up the block.
To pick up the block reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above block  2. Drop gripper around block  3. Close gripper around block
    Put the gripper above the block.
    - When the robot's gripper is not above block, move the robot's gripper until the robot's gripper is above block
    If the gripper isn't around the block, put it around the block.
    