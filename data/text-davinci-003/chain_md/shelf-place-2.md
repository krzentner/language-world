
    Steps:  1. Put gripper above block  2. Grab block with gripper  3. Move block to goal 
    First, put the gripper roughly above block, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above block, the robot should place gripper above block.
    If the gripper isn't around the block, put it around the block.
    - When the robot's gripper is not around block and the robot's gripper is open, the robot should drop gripper around block.
    If the gripper is near the block and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is near block and the robot's gripper is open, the robot should close gripper around block.
    We closed the gripper, and the block is still near the gripper, so maybe we grabbed it. Try to move the block to the goal. If we didn't grab it, it will just go back to an earlier step.
    - When the robot's gripper is above block and the robot's gripper is closed, the robot should move block to goal.