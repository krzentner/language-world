
    Steps:  1. Put gripper above cube  2. Drop gripper around cube  3. Close gripper around cube  4. Move cube to goal
    First, put the gripper roughly above cube, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the cube, move the robot's gripper until the robot's gripper is above the cube
    If the gripper isn't around the cube, put it around the cube.
    - When the robot's gripper is not around cube, move the robot's gripper until the robot's gripper is around the cube and the robot's gripper is closed
    If the gripper is around the cube, maybe we can grab it by closing the gripper.
    - When the robot's gripper is above cube, move the robot's gripper until the robot's gripper is near the target location

The task `pick-out-of` requires the robot to grab the cube and move it to the target location.
To grab the cube and move it to the target location reliably, what steps the robot should perform?
    Steps:  1. Put gripper above cube  2. Close gripper around cube  3. Lift gripper to drag cube out  4. Move cube to goal
    First, put the gripper roughly above cube, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above the cube, move the robot's gripper until the robot's gripper is above the cube
    If the robot's gripper is near the cube, we can try to grab it by closing the gripper around it.
    - When the robot's gripper is near the cube and the robot's gripper is closed, move the robot's gripper until the robot's gripper is around the cube
    If the gripper is around the cube, we can try to drag it out by lifting the gripper.
    - When the robot's gripper is around cube, move the robot's gripper until the robot's gripper is below the cube
    If the cube is in the air above the bowl, we can move it to the target location.
    - When the cube is not left of the robot's gripper, move the robot's gripper until the robot's gripper is above the target location

The task `stack` requires the robot to stack the cube onto the bowl.
To stack the cube onto the bowl reliably, what steps the robot should perform?
    Steps: