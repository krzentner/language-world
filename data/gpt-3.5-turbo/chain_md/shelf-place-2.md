To pick up the block and place it at the target location reliably, the robot should perform the following steps:

    Steps:  1. Put gripper above the block  2. Drop gripper around block  3. Close gripper around block  4. Lift the block  5. Move the block to the target location  6. Lower the block to place it down
    First, put the gripper roughly above the block, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the block, the robot should place gripper above the block.
    If the gripper isn't around the block, put it around the block.
    - When the robot's gripper is not around the block and the robot's gripper is open, the robot should drop gripper around the block.
    If the gripper is near the block and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is near the block and the robot's gripper is open, the robot should close gripper around the block.
    We closed the gripper, and the block is still near the gripper, now we can lift it up.
    - When the robot's gripper is closed around the block, the robot should lift the block.
    We can now move the block to the target location.
    - When the block is not at the target location, the robot should move the block to the target location.
    To place the block down, we should lower it now.
    - When the block is at the target location, the robot should lower the block to place it down.