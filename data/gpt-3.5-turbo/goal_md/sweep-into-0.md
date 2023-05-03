The task `sweep-into` requires the robot to use the gripper to sweep the cube into the goal area. To do this reliably, the robot should perform the following steps:

    Steps:  1. Put gripper near cube  2. Close gripper around cube  3. Lift cube up to prepare for sweeping  4. Move gripper to sweep the cube into the goal area

    First, put the gripper near the cube, so that we can grab it.
    - When the robot's gripper is not near the cube, move the robot's gripper until the robot's gripper is near the cube
    If the gripper isn't closed around the cube, close the gripper around the cube.
    - When the robot's gripper is near the cube and the robot's gripper is open, move the robot's gripper until the robot's gripper is around the cube and the robot's gripper is closed
    Lift up the cube so that we can prepare for sweeping.
    - When the robot's gripper is around the cube and the robot's gripper is closed, move the robot's gripper until the cube is lifted off the surface
    Finally, sweep the cube into the goal area, moving the gripper in a sweeping motion.
    - When the cube is lifted off the surface, move the robot's gripper in a sweeping motion and drop the cube when it is inside the goal area.