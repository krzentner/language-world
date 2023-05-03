To grab the cube and move it sideways to the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the cube  2. Grab the cube with the gripper  3. Move the gripper sideways to the goal while keeping the cube level  4. Release the cube at the goal
    First, put the gripper above the cube.
    - When the robot's gripper is not vertically aligned with the cube, the robot should put gripper above cube.
    As long as the gripper is still mostly around the cube, grab it.
    - When the robot's gripper is mostly around the cube and the gripper is open, the robot should grab the cube.
    Once the gripper has a good grip on the cube we can move it sideways to the goal while keeping the cube level so it doesn't drop.
    - When the robot's gripper is holding the cube and the robot's gripper is not near the goal, the robot should move the gripper sideways to the goal while keeping the cube level.
    Once the gripper and cube are at the goal, release the cube.
    - When the robot's gripper is above the goal and the gripper is closed around the cube, the robot should release the cube at the goal.