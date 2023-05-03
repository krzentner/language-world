To grab the cube and move it sideways to the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above cube  2. Drop gripper around cube  3. Close gripper around cube  4. Move cube sideways towards goal
    First, put the gripper above the cube.
    - When the robot's gripper is not above the cube, the robot should put gripper above the cube.
    If the gripper isn't around the cube, put it around the cube.
    - When the robot's gripper is not around the cube and the robot's gripper is open, the robot should drop gripper around the cube.
    If the gripper is near the cube and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is near the cube and the robot's gripper is open, the robot should close gripper around the cube.
    We closed the gripper, and the cube is still near the gripper. Move the cube sideways towards the goal.
    - When the robot's gripper is closed and the cube is not at the goal position, the robot should move cube sideways towards the goal position.