
    Steps:  1. Put gripper above the cube  2. Grab the cube  3. Move the cube sideways
    First, put the gripper above the cube.
    - When the robot's gripper is not vertically aligned with the cube, the robot should put gripper above cube.
    As long as the gripper is above the cube and the cube is still below the gripper, we can grab the cube by closing the gripper.
    - When the robot's gripper is above the cube and the robot's gripper is open, the robot should grab cube.
    We closed the gripper, and the cube is still near the gripper, so maybe we grabbed it. Try to move the cube to the target location. If we didn't grab it, we'll just go back to an earlier step.
    - When the robot's gripper is above cube and the robot's gripper is closed, the robot should move cube sideways to target location.