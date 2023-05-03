The task `sweep-into` requires the robot to grab the cube by sweeping it into the gripper and then move it to the target location. To do this reliably, the robot should perform the following steps:

    Steps:  1. Place gripper near cube  2. Sweep gripper into cube to grab it  3. Lift cube up  4. Move cube to target location  5. Release cube

    First, the robot should place the gripper near the cube.
    - When the robot's gripper is not near the cube, the robot should move the gripper near the cube.
    Once the gripper is near the cube, the robot should sweep it into the gripper to grab it.
    - When the cube is near the gripper, the robot should sweep the gripper into the cube and close the gripper to grab it.
    Once the cube is grabbed, the robot should lift it up.
    - When the gripper is closed around the cube, the robot should lift the cube up in the gripper.
    Next, move the cube to the target location.
    - When the robot's gripper is holding the cube and the cube is not at the target location, the robot should move the gripper to the target location.
    Finally, release the cube.
    - When the robot's gripper is at the target location holding the cube, the robot should release the cube.