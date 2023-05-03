The task `sweep` requires the robot to grab the cube and move sideways it to the target location.
To grab the cube and move sideways it to the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above cube  2. Grab cube with the gripper  3. Move gripper and cube towards the target location
    First, put the gripper roughly above the cube.
    - When the robot's gripper is not above the cube, move the robot's gripper until the robot's gripper is above the cube
    If the gripper isn't around the cube, put it around the cube.
    - When the robot's gripper is not around the cube and the robot's gripper is open, move the robot's gripper until the robot's gripper is near the cube and the robot's gripper is closed
    If the gripper is near the cube and closed, we can grab it and move it towards the target location.
    - When the robot's gripper is closed around the cube, move the robot's gripper and cube sideways towards the target location.