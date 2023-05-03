To pick up the cube and place it in the target bin reliably, the robot should perform the following steps:
    Steps:  1. Detect and locate the cube and the target bin  2. Move the gripper above the cube  3. Drop gripper around cube  4. Close gripper around cube  5. Lift the cube  6. Move the gripper to the target bin  7. Move the gripper above the target bin  8. Open gripper to drop the cube in the bin
First, use sensors to detect and locate the cube and the target bin.
    - When the cube or the bin is not detected, the robot should stop and wait for the object to appear in the field of view of the sensors
Once the cube is detected, move the gripper above it.
    - When the robot's gripper is not above the cube, move the robot's gripper until the robot's gripper is above the cube
If the gripper isn't around the cube, put it around the cube.
    - When the robot's gripper is not around the cube and the robot's gripper is open, move the robot's gripper until the robot's gripper is near the cube and the robot's gripper is closed
If the gripper is around the cube, we can use it to pick it up. Lift the cube by moving the gripper up.
    - When the cube is trapped by the gripper and the robot's gripper is not above the cube, move the robot's gripper until the robot's gripper is above the cube
Move the gripper to the target bin.
    - When the robot's gripper is not near the target bin, move the robot's gripper until the robot's gripper is near the target bin
Move the gripper above the target bin, so that we can drop the cube in.
    - When the robot's gripper is not above the target bin, move the robot's gripper until the robot's gripper is above the target bin
Open the gripper to drop the cube in the bin.
    - When the robot's gripper is above the target bin and the robot's gripper is closed, open the robot's gripper to drop the cube in the target bin