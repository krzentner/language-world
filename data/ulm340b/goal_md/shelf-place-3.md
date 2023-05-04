

The task `shelf-place` requires the robot to pick up the block and place it at the target location.
To pick up the block and place it at the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above block  2. Grab block with gripper  3. Pick block up  4. Move block to target location
    First, put the gripper mostly above the block.
    - When the robot's gripper is not vertically aligned with the block, move the robot's gripper until the robot's gripper is vertically aligned with the block and the robot's gripper is closed
    If the block becomes right of the gripper, go back to putting the gripper above the block. Because the block is a small object, check if the gripper is around it.
    - When the block is not right of the robot's gripper and the block is not around the robot's gripper, move the robot's gripper until the robot's gripper is around the block
    As long as the block is mostly around the gripper, the robot should be able to pick it up by moving up.
    - When the block is around the robot's gripper, move the robot's gripper until the robot's gripper is below the block
    If the block is below the gripper, we can try to place it at the target location.
    - When the block is not below the robot's gripper, move the robot's gripper until the robot's gripper is above the target location

The task `peg-insert-topdown` requires the robot to grab the peg and insert it into the hole from above.
To grab the peg and insert it into the hole from above reliably, what steps the robot should perform?

The task `peg-insert-topdown` requires the robot to grab the peg and insert it into the hole from above.
To grab the peg and insert it into the hole from above reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Drop gripper around peg  3. Line the peg up with the hole  4. Push the peg into the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, move the robot's gripper until the robot's gripper is vertically aligned with the peg
    Once the gripper is lined up above the peg, we should be able to grab it by moving the gripper down around it.
    - When the peg is above the robot's gripper