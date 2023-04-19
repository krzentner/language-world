To pick up the block and place it at the target location, the robot should perform the following steps:
    Steps:  1. Put gripper above block  2. Drop gripper around block  3. Close gripper around block  4. Move block to goal location  5. Open gripper to release the block
    First, put the gripper above the block so that we don't bump into it while trying to grab it.
    - When the robot's gripper is not above the block, move the robot's gripper until it is above the block
    If the gripper is not around the block, put it around the block.
    - When the robot's gripper is not around the block and the robot's gripper is open, move the robot's gripper until it is near the block and the robot's gripper is closed
    If the gripper is near the block and closed, grab it by holding the block securely in the gripper.
    - When the robot's gripper is above the block and the gripper is closed, move the robot's gripper until it is near the target location
    If the gripper is near the target location, place the block by opening the gripper to release the block.
    - When the robot's gripper is near the target location and the gripper is closed around the block, move the robot's gripper until it is above the target location and the gripper is open