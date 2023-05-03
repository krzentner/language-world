For the task `sweep-into` where the robot has to grab the cube and move it to the target location, the following steps can be performed:
    
    Steps:  1. Put gripper above the cube  2. Grab the cube with the gripper  3. Move the cube to the target location
    First, put the gripper above the cube.
    - When the robot's gripper is not vertically aligned with the cube, move the robot's gripper until the robot's gripper is vertically aligned with the cube
    If the gripper isn't around the cube, put it around the cube.
    - When the robot's gripper is not around the cube and the robot's gripper is open, move the robot's gripper until the robot's gripper is near the cube and the robot's gripper is closed
    If the gripper is near the cube and closed, we've probably grabbed the cube and move it to the target location.
    - When the robot's gripper is closed and the cube is not at the target location, move the cube to the target location using the gripper.