To pick up the block and place it at the target location reliably for the `shelf-place` task, the robot should perform the following steps:

    Steps:  1. Put gripper above block approximately  2. Move gripper towards the block to grab it  3. Grip the block  4. Lift the block above the shelf  5. Move to the target location  6. Move the gripper down to lower the block onto the shelf
    First, put the gripper roughly above the block. We don't need to be super precise, just get it in the general area.
    - When the robot's gripper is not above the block, move the robot's gripper until the robot's gripper is above the block
    Once the gripper is above the block, move the gripper towards the block to grab it.
    - When the robot's gripper is not around the block, move the robot's gripper until the robot's gripper is around the block
    Make sure the gripper has a good grip on the block before lifting it up.
    - When the robot's gripper is around the block, move the robot's gripper up until the block is above the shelf and the robot's gripper is vertically aligned with the shelf
    Move the gripper to the target location while holding on to the block.
    - When the robot's gripper is not near the target location, move the robot's gripper until the robot's gripper is near the target location
    Finally, move the gripper down to lower the block onto the shelf.
    - When the robot's gripper is near the target location, move the robot's gripper down until the block is on the shelf and the robot's gripper is open