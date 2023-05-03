To pick up the block and place it at the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the block  2. Drop gripper around the block  3. Close gripper around the block  4. Move block to the target location  5. Release the gripper and drop the block at the target location
    First, put the gripper above the block, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the block, the robot should place gripper above the block.
    If the gripper isn't around the block, put it around the block.
    - When the robot's gripper is not around the block and the robot's gripper is open, the robot should drop gripper around the block.
    If the gripper is near the block and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is near the block and the robot's gripper is open, the robot should close the gripper around the block.
    We closed the gripper, and the block is still near the gripper, so maybe we grabbed it. Try to move the block to the target location. If we didn't grab it, we'll just go back to an earlier step.
    - When the robot's gripper is above the target location and the robot's gripper is closed around the block, the robot should move the block to the target location.
    Once we've moved the block to the target location, we can release the gripper and drop the block at the target location.
    - When the robot's gripper is above the target location and the robot's gripper is closed around the block, the robot should release the gripper and drop the block at the target location.