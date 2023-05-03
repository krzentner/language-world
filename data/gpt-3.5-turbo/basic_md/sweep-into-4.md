To grab the cube and move it to the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the cube, the robot should put gripper above the cube.
    - When the robot's gripper is vertically aligned with the cube and the robot's gripper is not near the cube, the robot should grab the cube.
    - When the robot's gripper is holding the cube and the robot is not facing the target location, the robot should turn towards the target location.
    - When the robot is facing the target location and the robot's gripper is not near the target location, the robot should move towards the target location.
    - When the robot's gripper is near the target location, the robot should release the cube and place it in the target location.