To pick up the cube and place it in the target bin reliably, the robot should perform the following steps:
    Steps:  1. Find the cube with the robot's vision system  2. Plan a path to reach the cube  3. Move the robot's gripper above the cube  4. Drop gripper around the cube  5. Close gripper around the cube  6. Plan a path to the target bin  7. Move the gripper to the target bin  8. Open gripper to drop the cube into the bin
First, the robot needs to locate the cube with its vision system. Once the cube is identified, the robot needs to plan a path for the gripper to reach the cube without knocking it over or colliding with other objects.
    - When the cube is not in the robot's vision, move the robot until the cube is detected
    - When the cube is detected, plan a path from the current position to the cube's location without collision
Next, the robot should move the gripper above the cube and line it up vertically with the cube. Then the gripper should be lowered around the cube and closed to hold onto it.
    - When the robot's gripper is not above the cube, move the robot's gripper until the robot's gripper is above the cube
    - When the robot's gripper is not vertically aligned with cube, move the robot's gripper until the robot's gripper is vertically aligned with the cube
    - When the robot's gripper is not around the cube, move the robot's gripper until the robot's gripper is near the cube and the gripper is closed
Once the cube is securely gripped, the robot should plan a path to the target bin without colliding with other objects. The gripper should move to the target bin and the gripper should be opened to drop the cube inside the bin.
    - When the robot's gripper is not in a collision-free path to the target bin, replan the path to the target bin
    - When the robot's gripper is near the target bin, move the robot's gripper to the target bin
    - When the robot's gripper is above the bin, open the gripper to drop the cube into the bin.