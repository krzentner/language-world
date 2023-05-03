To pick up the block and place it at the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above block  2. Drop gripper around block  3. Close gripper around block  4. Lift block up  5. Move block to the target location  6. Lower block down  7. Open gripper to release the block
    First, put the gripper roughly above the block, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the block, the robot should place gripper above the block.
    If the gripper isn't around the block, put it around the block.
    - When the robot's gripper is not around the block and the robot's gripper is open, the robot should drop gripper around the block.
    If the gripper is near the block and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is near the block and the robot's gripper is open, the robot should close the gripper around the block.
    We closed the gripper, and the block is still attached to the surface, so we probably grabbed it. Lift the block up.
    - When the robot's gripper is closed around the block and the block is attached to the surface, the robot should lift the block up.
    Move the block to the target location.
    - When the robot is holding the block, the robot should move the block to the target location.
    Once the block is near the target location, lower the block down to place it at the target location.
    - When the robot's gripper is above the target location, the robot should lower the block down to place it at the target location.
    Finally, open the gripper to release the block.
    - When the block has been placed at the target location, the robot should open the gripper to release the block.