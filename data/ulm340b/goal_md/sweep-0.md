
    Steps:  1. Put gripper above cube  2. Drop gripper around cube  3. Close gripper around cube  4. Slide cube to goal
    First, put the gripper roughly above cube, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above cube, move the robot's gripper until the robot's gripper is above cube
    If the gripper isn't around the cube, put it around the cube.
    - When the robot's gripper is not around cube and the robot's gripper is open, move the robot's gripper until the robot's gripper is near cube and the robot's gripper is closed
    If the gripper is near the cube and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is around cube and the robot's gripper is closed, move the robot's gripper until the robot's gripper is forward aligned with the target location

The task `block-stack` requires the robot to put the cube on top of the block.
To put the cube on top of the block reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above cube  2. Drop gripper around cube  3. Close gripper around cube  4. Move gripper up to a good drop position above the block  5. Release gripper
    First, put the gripper roughly above cube, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above cube, move the robot's gripper until the robot's gripper is above cube
    If the gripper isn't around the cube, put it around the cube.
    - When the robot's gripper is not around cube and the robot's gripper is open, move the robot's gripper until the robot's gripper is near cube and the robot's gripper is closed
    If the gripper is near the cube and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is above cube and the robot's gripper is closed, move the robot's gripper until the robot's gripper is near block
    If the gripper is not open, we can't release the cube yet.
    - When the robot's gripper is near block and the robot's gripper is open, move the robot's gripper until the robot's gripper is almost vertically aligned with block
  