
    Steps:  1. Put gripper above the block  2. Grab the block with the gripper  3. Move the block to the target location
    First, put the gripper above the block.
    - When the robot's gripper is not above the block and the robot's gripper is not vertically aligned with the block, move the robot's gripper until the robot's gripper is vertically aligned with the block
    As long as the gripper is still mostly around the block, the block should remain in the gripper.
    - When the robot's gripper is vertically aligned with the block and the block is not near the robot's gripper, move the robot's gripper until the robot's gripper is around the block and the robot's gripper is closed
    - When the robot's gripper is around the block and the block is not near the target location, move the robot's gripper until the robot's gripper is near the target location
    If the block is near the target location, we can put it down by opening the gripper.
    - When the robot's gripper is near the target location, move the robot's gripper until the robot's gripper is open

The task `button-press-side` requires the robot to push the button from the side.
To push the button from the side reliably, the robot should perform the following steps:
    Steps:  1. Put the gripper above the button  2. Push gripper down into the button
    First, put the gripper above the button.
    - When the robot's gripper is not above the button and the robot's gripper is not vertically aligned with the button, move the robot's gripper until the robot's gripper is vertically aligned with the button
    If the button is not to the side of the gripper, we can probably push the button down by moving the gripper down and closing the gripper.
    - When the robot's gripper is vertically aligned with the button and the robot's gripper is not around the button, move the robot's gripper until the robot's gripper is horizontally aligned with the button and the robot's gripper is closed

The task `pick-place-side` requires the robot to pick up the block and put it down at the target location.
To pick up the block and put it down at the target location reliably, the robot should perform the following steps:
    Steps:  1. Put the gripper above the block  2. Drop the gripper around the block  3. Close the gripper around the block  4. Put the