
    Steps:  1. Put gripper above cube  2. Drop gripper around cube  3. Close gripper around cube  4. Move cube to goal
    First, put the gripper above cube.
    - When the robot's gripper is not vertically aligned with cube, the robot should put gripper above cube.
    If the gripper isn't around the cube, line it up and put it around the cube.
    - When the robot's gripper is not around cube and the robot's gripper is open, the robot should drop gripper around cube.
    If the gripper is near the cube and open, we can grab the cube by closing the gripper.
    - When the robot's gripper is near cube and the robot's gripper is open, the robot should close gripper around cube.
    We've closed the gripper, and the cube is still close to the gripper, so we might have grabbed it. Try to move the cube to the goal. If we didn't grab it, go back to an earlier step.
    - When the robot's gripper is closed around the cube, the robot should move the cube to the goal.