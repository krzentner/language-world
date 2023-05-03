The task `shelf-place` requires the robot to pick up the block and place it at the target location.
To pick up the block and place it at the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the block  2. Grab the block with the gripper firmly  3. Lift the block up to a safe height  4. Move the block to the target location  5. Release the block 
    First, put the gripper roughly above the block.
    - When the robot's gripper is not above the block, move the robot's gripper until the robot's gripper is above the block
    If the gripper isn't around the block, put it around the block.
    - When the robot's gripper is not around the block and the robot's gripper is open, move the robot's gripper until the robot's gripper is near the block and the robot's gripper is closed
    Once the gripper is holding the block, lift it up to a safe height so that it clears any obstructions.
    - When the block is being lifted and the robot's gripper is closed, move the robot's gripper until the robot's gripper is near the target location
    Move the block to the target location and release it.
    - When the block is above the target location and the robot's gripper is closed, release the block.