Here are the steps the robot should follow for the `bin-picking` task:

1. Put the gripper above the cube
- When the robot's gripper is not above the cube, move the robot's gripper until the robot's gripper is above the cube
2. Open the gripper and drop it around the cube
- When the robot's gripper is not around the cube and the robot's gripper is closed, move the robot's gripper until the robot's gripper is near the cube and the robot's gripper is open
3. Close the gripper and lift the cube
- When the robot's gripper is around the cube and the robot's gripper is open, close the robot's gripper around the cube and lift the cube
4. Move the gripper above the target bin and release the cube
- When the robot's gripper is not above the target bin, move the robot's gripper until the robot's gripper is above the target bin
- When the robot's gripper is above the target bin and the robot's gripper is closed around the cube, release the cube into the target bin