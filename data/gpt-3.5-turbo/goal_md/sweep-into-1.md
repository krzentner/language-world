The task `sweep-into` requires the robot to grab the cube and move it to the target location. To do this reliably, the robot should perform the following steps:

1. Put the gripper near the cube and open it.
2. Move the gripper towards the cube until it is touching it.
3. Close the gripper around the cube to grab it.
4. Move the gripper with the cube towards the target location.
5. When the gripper is near the target location, release the cube by opening the gripper.

If the gripper is not initially near the cube, move it close to the cube to start the grabbing process.
- When the robot's gripper is not near the cube, move the robot's gripper until the robot's gripper is near the cube

If the gripper is not touching the cube after moving it near the cube, move it until it is touching the cube.
- When the robot's gripper is near the cube and the gripper is not touching the cube, move the robot's gripper until the gripper is touching the cube

If the gripper is not closed around the cube after touching it, close it.
- When the robot's gripper is touching the cube and the gripper is not closed around the cube, close the gripper around the cube

If the gripper is not near the target location after grabbing the cube, move it towards the target location.
- When the robot's gripper is closed around the cube and the gripper is not near the target location, move the gripper with the cube towards the target location. 

Lastly, release the cube when the gripper is near the target location.
- When the robot's gripper is near the target location, release the cube by opening the gripper.