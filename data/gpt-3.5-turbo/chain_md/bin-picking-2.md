To pick up the cube and place it in the target bin reliably, the robot should perform the following steps:
    Steps:  1. Find the cube with the camera  2. Move the gripper above the cube  3. Drop the gripper around the cube  4. Raise the gripper with the cube inside  5. Move the gripper to the target bin  6. Lower the gripper until the cube is inside the bin  7. Release the gripper to drop the cube into the bin
    First, the robot should use the camera to locate the cube.
    - When the cube is not in view of the camera, the robot should move the camera to locate the cube.
    Once the cube is located, move the gripper above the cube with enough clearance.
    - When the robot's gripper is not above the cube, the robot should move gripper above the cube.
    Move the gripper down to drop around the cube, making sure that the cube is fully inside the gripper and centered.
    - When the robot's gripper is not around the cube and the robot's gripper is open, the robot should drop gripper around the cube.
    Raise the gripper with the cube held inside, making sure it is secure.
    - When the robot's gripper is around the cube, the robot should raise gripper with the cube.
    Move the gripper towards the target bin, making sure to avoid any obstacles in the way.
    - When the robot's gripper is not near the target bin, the robot should move gripper towards the target bin.
    Lower the gripper until the cube is inside the bin, and make sure it is centered.
    - When the robot's gripper is above the target bin and the robot's gripper is not lowered with the cube centered inside the bin, the robot should lower the gripper until the cube is inside the bin and centered.
    Release the gripper to drop the cube into the bin.
    - When the robot's gripper is lowered with the cube inside the bin, the robot should release the gripper to drop the cube into the bin.