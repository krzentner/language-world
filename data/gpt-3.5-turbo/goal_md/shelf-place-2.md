The task `shelf-place` requires the robot to pick up the block and place it at the target location.
To pick up the block and place it at the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the block  2. Drop gripper around the block  3. Close gripper around the block  4. Lift the block off the shelf  5. Move gripper to target location  6. Release the block at the target location
Firstly, put the gripper roughly above the block, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the block, move the robot's gripper until the robot's gripper is above the block
If the gripper isn't around the block, put it around the block.
    - When the robot's gripper is not around the block and the robot's gripper is open, move the robot's gripper until the robot's gripper is near the block and the robot's gripper is closed
If the gripper is near the block and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is around the block and the robot's gripper is closed, move the robot's gripper upwards until the block is lifted off the shelf
Once the block is lifted off the shelf, move the gripper to the target location.
    - When the robot's gripper is not near the target location, move the robot's gripper until the robot's gripper is near the target location
Finally, release the block at the target location.
    - When the robot's gripper is near the target location and the robot's gripper is closed, open the robot's gripper to release the block at the target location.