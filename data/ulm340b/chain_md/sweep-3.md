
    Steps:  1. Put gripper above cube  2. Drop gripper around cube  3. Close gripper around cube  4. Move cube sideways to goal
    First, put the gripper roughly above cube, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the cube, the robot should place gripper above cube.
    If the gripper isn't around the cube, put it around the cube.
    - When the robot's gripper is not around cube and the robot's gripper is open, the robot should drop gripper around cube.
    If the gripper is near the cube and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is near cube and the robot's gripper is open, the robot should close gripper around cube.
    We closed the gripper, and the cube is still near the gripper, so maybe we grabbed it. Try to sweep the cube to the goal. If we didn't grab it, we'll just go back to an earlier step.
    - When the robot's gripper is above cube and the robot's gripper is closed, the robot should move cube sideways to the goal.

The task `stack` requires the robot to pick up the cube and hold it on top of the target.
To pick up the cube and hold it on top of the target reliably, what steps the robot should perform?
    Steps:  1. Put gripper above cube  2. Drop gripper around cube  3. Close gripper around cube  4. Lift cube to place on top of target
    First, put the gripper roughly above cube, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the cube, the robot should place gripper above cube.
    If the gripper isn't around the cube, put it around the cube.
    - When the robot's gripper is not around cube and the robot's gripper is open, the robot should drop gripper around cube.
    If the gripper is near the cube and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is near cube and the robot's gripper is open, the robot should close gripper around cube.
    We closed the gripper, and the cube is still near the gripper, so maybe we grabbed it. Lift the cube and place it on the target.
    - When the robot's gripper is above cube and the robot'