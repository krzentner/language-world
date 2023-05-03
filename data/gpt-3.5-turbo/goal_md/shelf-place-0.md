To pick up the block and place it at the target location reliably, the robot should perform the following steps:

    Steps:  1. Put gripper above block  2. Drop gripper around block  3. Close gripper around block  4. Move block to target location  5. Open gripper to release block
    First, put the gripper above the block, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the block, move the robot's gripper until the robot's gripper is above the block
    If the gripper isn't around the block, put it around the block.
    - When the robot's gripper is not around the block and the robot's gripper is open, move the robot's gripper until the robot's gripper is near the block and the robot's gripper is closed
    If the gripper is near the block and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is above the block and the robot's gripper is closed, move the robot's gripper until the robot's gripper is above the target location
    Once the robot's gripper is above the target location, move the block to the target location.
    - When the robot's gripper is above the target location and the robot's gripper is closed, move the robot's gripper until the robot's gripper is above the target location and the robot's gripper is open.