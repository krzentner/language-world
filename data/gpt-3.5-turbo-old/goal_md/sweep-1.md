The task `sweep` requires the robot to grab the cube and move sideways it to the target location.
To grab the cube and move sideways it to the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the cube  2. Drop gripper around the cube  3. Close gripper around the cube
    To start, put the gripper above the cube.
    - When the robot's gripper is not above the cube, move the robot's gripper until the robot's gripper is above the cube
    Once the gripper is above the cube, drop the gripper around the cube.
    - When the robot's gripper is above the cube and the robot's gripper is open, move the robot's gripper until the robot's gripper is near the cube and the robot's gripper is closed
    If the gripper is around the cube, we can now slide the cube to the target location.
    - When the robot's gripper is around the cube, move the robot's gripper horizontally to the target location while keeping the cube gripped.