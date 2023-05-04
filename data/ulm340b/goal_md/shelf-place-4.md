
    Steps:  1. Put gripper above the block  2. Drop gripper around the block  3. Close gripper around block  4. Move block to the target

The task `shelf-place` requires the robot to pick up the block and place it at the target location.
To pick up the block and place it at the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the block  2. Drop gripper around the block  3. Close gripper around block  4. Move block to the target
    First, put the gripper roughly above the block, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the block, move the robot's gripper until the robot's gripper is above the block
    If the gripper isn't around the block, put it around the block.
    - When the robot's gripper is not around block and the robot's gripper is open, move the robot's gripper until the robot's gripper is near the block and the robot's gripper is closed
    If the gripper is near the block and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is above block and the robot's gripper is closed, move the robot's gripper until the robot's gripper is near the target

The task `shelf-remove` requires the robot to grab the block from the shelf and move it away.
To grab the block from the shelf and move it away reliably, what steps the robot should perform?
    Steps:  1. Put gripper above the block  2. Drop gripper around the block  3. Close gripper around block  4. Move block away from shelf

The task `shelf-remove` requires the robot to grab the block from the shelf and move it away.
To grab the block from the shelf and move it away reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the block  2. Drop gripper around the block  3. Close gripper around block  4. Move block away from shelf
    First, put the gripper roughly above the block, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the block, move the robot's gripper until the robot's gripper is above the block
    If the gripper isn't around the block, put it around the block.
    - When the robot'