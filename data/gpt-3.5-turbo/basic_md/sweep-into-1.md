To grab the cube and move it to the target location reliably, the robot should perform the following steps for the `sweep-into` task:

- When the robot's gripper is not above the cube, the robot should place the gripper above the cube.
- When the robot's gripper is not open and not around the cube, the robot should open the gripper.
- When the robot's gripper is near the cube and open, the robot should close the gripper around the cube.
- When the robot's gripper is holding the cube, the robot should move the gripper to the target location.
- When the robot's gripper is above the target location, the robot should release the cube by opening the gripper.