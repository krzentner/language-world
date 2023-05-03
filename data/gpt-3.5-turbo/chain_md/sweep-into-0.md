For the task `sweep-into`, the robot should perform the following steps:

Steps: 1. Position gripper next to cube, with gripper claws facing towards the cube, and with the claws open. 
2. Move gripper towards the cube, closing the claws around the cube. 
3. Lift the cube slightly off the ground. 
4. Move the gripper with the cube towards the target location, while keeping the cube at a low height (so it doesn't bump into anything). 
5. Once the target location is reached, place the cube down gently. 
6. Open the gripper claws to release the cube. 

If the robot is not positioned next to the cube, it should first move to a position next to the cube. 
- When the robot's gripper is not next to the cube, the robot should move gripper to the side of the cube. 

If the gripper is not facing the cube, it should turn the gripper in the correct orientation.
- When the gripper is not facing the cube, the robot should position the gripper with the claws facing towards the cube. 

If the gripper claws are not open, it should open them.
- When the robot's gripper is not open, the robot should open the claws. 

If the robot's gripper is not closed around the cube and the robot's gripper is near the cube, it should close the claws around the cube.
- When the robot's gripper is near the cube and the robot's gripper is not closed around the cube, the robot should close the claws around the cube. 

If the cube is positioned too high above the ground, the robot should lower it to the correct height.
- When the cube is not at the correct height, the robot should adjust the height of the gripper to move the cube while keeping it at a low height. 

If the robot is not yet at the target location, it should continue to move towards it.
- When the robot's gripper is not at the target location, the robot should continue moving towards the target location. 

If the robot's gripper is not open when it's at the target location, it should open the claws to release the cube. 
- When the robot's gripper is at the target location and the robot's gripper is closed, the robot should open the claws to release the cube.