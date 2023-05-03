To grab the cube and move it to the target location reliably for the task `sweep-into`, the robot should perform the following steps:

    Steps:  1. Put gripper above the cube  2. Close gripper around the cube  3. Move the cube to the target location
    First, put the gripper above the cube.
    - When the robot's gripper is not above the cube, move the robot's gripper until the robot's gripper is above the cube
    Once the gripper is above the cube, close the gripper around it to grab it.
    - When the robot's gripper is above the cube and the robot's gripper is open, move the robot's gripper until the robot's gripper is near the cube and the robot's gripper is closed
    If the gripper is near the cube, we can just move the gripper with the cube towards the target location.
    - When the robot's gripper is closed around the cube and the cube is not at the target location, move the robot's gripper until the cube is at the target location.