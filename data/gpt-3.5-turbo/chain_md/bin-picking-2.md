To pick up the cube and place it in the target bin reliably, the robot should perform the following steps:
    Steps:  1. Detect cube and bin  2. Plan the grasp and movement trajectory  3. Move gripper to above the cube  4. Close gripper around the cube  5. Move gripper to above the target bin  6. Release the cube into the bin
    First, detect the cube and target bin, and plan the grasp and movement trajectory.
    - When the cube and target bin are not detected, the robot should search for them.
    Move the gripper to be above the cube, making sure that there is enough clearance between the gripper and the cube.
    - When the robot's gripper is not above the cube, the robot should move the gripper to be above the cube.
    Close the gripper around the cube until it is secure.
    - When the robot's gripper is above the cube and is not closed, the robot should close the gripper around the cube.
    Move the gripper to above the target bin with enough clearance to ensure the cube doesn't hit the bin on the way down.
    - When the robot's gripper is not above the target bin, the robot should move the gripper to be above the target bin.
    Release the cube into the target bin by opening the gripper.
    - When the robot's gripper is above the target bin and is not open, the robot should release the cube into the bin.