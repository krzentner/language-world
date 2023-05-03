The task `bin-picking` can be broken down into the following steps:
    Steps:  1. Identify the cube to pick up  2. Put gripper above cube  3. Drop gripper around cube  4. Close gripper around cube  5. Move cube to target bin  6. Open gripper to release cube
First, the robot needs to identify which cube to pick up. Once identified, put the gripper above the cube.
    - When the robot's gripper is not above the cube, the robot should put gripper above cube.
If the gripper is not around the cube, move it down to the cube and drop the gripper around it.
    - When the robot's gripper is not around the cube and the robot's gripper is open, the robot should drop gripper around cube.
Close the gripper to pick up the cube.
    - When the robot's gripper is near the cube and the robot's gripper is open, the robot should close gripper around cube.
Once the cube is grasped, move it to the target bin.
    - When the robot's gripper is closed around the cube and the robot's gripper is not above target bin, the robot should move cube to target bin.
Finally, open the gripper to release the cube into the target bin.
    - When the robot's gripper is above target bin and the robot's gripper is closed around the cube, the robot should open gripper to release cube.