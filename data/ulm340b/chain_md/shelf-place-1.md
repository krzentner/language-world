
    Steps:  1. Line up the robot's gripper from above  2. Drop the gripper down around the block  3. Move the block to the target
    Because this is "side", we just need to line up the gripper from the side. Line up the robot's gripper from the side.
    - When the robot's gripper is not horizontally aligned with the block, the robot should align gripper horizontally.
    Once the gripper is lined up above the block, we should be able to grab the block by moving the gripper down around it.
    - When the robot's gripper is horizontally aligned with the block and the robot's gripper is not around the block, the robot should grab the block.
    If the block is still near the robot's gripper, try to place the block at the target.
    - When the block is near the robot's gripper, the robot should place the block on the shelf.

The task `shelf-align` requires the robot to align the block to the target position by sliding it sideways.
To align the block to the target position by sliding it sideways reliably, what steps the robot should perform?
    Steps:  1. Line up the gripper from the side  2. Drop the gripper down around the block  3. Slide the block into place
    Because this is "side", we just need to line up the gripper from the side. Line up the robot's gripper from the side.
    - When the robot's gripper is not horizontally aligned with the block, the robot should align gripper horizontally.
    Once the gripper is lined up above the block, we should be able to grab the block by moving the gripper down around it.
    - When the robot's gripper is horizontally aligned with the block and the robot's gripper is not around the block, the robot should grab the block.
    If the gripper is around the block, move the block to the target.
    - When the robot's gripper is around the block and the block is not horizontally aligned with the goal, the robot should align block horizontally.

The task `shelf-regrasp` requires the robot to regrasp the block and place it at the target location.
To regrasp the block and place it at the target location reliably, what steps the robot should perform?
    Steps:  1. Grab the block  2. Move the block to the target
    Pick the block up, then try to put it down.
    - When the block is not vertically aligned with the robot's gripper, the robot should grab the block.
   