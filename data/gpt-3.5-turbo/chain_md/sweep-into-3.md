The task `sweep-into` requires the robot to grab the cube and move it to the target location reliably. To accomplish this task, the robot should perform the following steps:

Steps:  1. Put gripper above the cube  2. Drop gripper around the cube  3. Close gripper around the cube  4. Lift the cube off the ground and move it towards the target location 5. Release the cube at the target location.

First, put the gripper roughly above the cube to avoid knocking it over while picking it up.
- When the robot's gripper is not above the cube, the robot should put gripper above the cube.
Once the gripper is above the cube, drop it around the cube.
- When the robot's gripper is not around the cube and the robot's gripper is open, the robot should drop gripper around the cube.
Check if the gripper is closed around the cube. If not, close it.
- When the robot's gripper is around the cube and the robot's gripper is open, the robot should close gripper around the cube.
Lift the cube off the ground and move it towards the target location.
- Once the gripper is closed around the cube, lift it off the ground and move it towards the target location.
When the cube reaches the target location, release it.
- When the robot's gripper is above the target location, the robot should release the cube at the target location.