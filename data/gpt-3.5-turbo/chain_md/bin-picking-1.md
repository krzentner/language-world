To pick up the cube and place it in the target bin, the robot should perform the following steps:
    Steps:  1. Put gripper above cube  2. Drop gripper around cube  3. Close gripper around cube  4. Move cube to target bin  5. Drop cube in target bin
    First, put the gripper roughly above the cube.
    - When the robot's gripper is not above the cube, the robot should place gripper above cube.
    If the gripper isn't around the cube, put it around the cube.
    - When the robot's gripper is not around the cube and the robot's gripper is open, the robot should drop gripper around cube.
    If the gripper is near the cube and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is near the cube and the robot's gripper is open, the robot should close gripper around cube.
    We closed the gripper, and the cube is still near the gripper, so maybe we grabbed it. Try to move the cube to the target bin. If we didn't grab it, we'll just go back to an earlier step.
    - When the robot's gripper is above the target bin and the robot's gripper is closed, the robot should drop cube in target bin.