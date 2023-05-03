The task `sweep-into` requires the robot to grab the cube and move it to the target location.
To grab the cube and move it to the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper roughly over the cube  2. Drop gripper around the cube  3. Close gripper around the cube  4. Sweep the cube towards the goal  5. Raise the gripper to place the cube in the goal
    First, put the gripper roughly over the cube.
    - When the robot's gripper is not above the cube, the robot should place gripper above cube.
    If the gripper isn't around the cube, put it around the cube.
    - When the robot's gripper is not around cube and the robot's gripper is open, the robot should drop gripper around cube.
    If the gripper is near the cube and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is near cube and the robot's gripper is open, the robot should close gripper around cube.
    Once the cube is grabbed by the gripper, sweep it towards the goal.
    - When the robot's gripper is holding the cube and the robot's gripper is not vertically aligned with the goal, the robot should sweep the cube towards the goal.
    Once the cube is positioned over the goal, raise the gripper to place the cube inside the goal.
    - When the robot's gripper is holding the cube and the robot's gripper is vertically aligned with the goal, the robot should raise the gripper to place the cube inside the goal.