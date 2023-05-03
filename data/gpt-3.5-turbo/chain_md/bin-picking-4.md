The task `bin-picking` requires the robot to pick up the cube and place it in the target bin. To do this reliably, the robot should perform the following steps:

    Steps:  1. Put gripper above the cube. 2. Drop gripper around the cube. 3. Close gripper around the cube. 4. Move the cube towards the target bin. 5. Drop the cube in the bin.

    First, put the gripper above the cube, so that we don't accidentally hit the cube while trying to grab it.
    - When the robot's gripper is not above the cube, the robot should put gripper above the cube.
    If the gripper is not around the cube, put it around the cube.
    - When the robot's gripper is not around the cube and the robot's gripper is open, the robot should drop gripper around the cube.
    If the gripper is near the cube and open, we can try to grab it by closing the gripper.
    - When the robot's gripper is near the cube and the robot's gripper is open, the robot should close the gripper around the cube.
    We closed the gripper, and the cube is still near the gripper, so we probably grabbed it. Move the cube towards the target bin.
    - When the robot's gripper is holding the cube and the robot's gripper is not near the target bin, the robot should move the cube towards the target bin.
    Once we're near the target bin, drop the cube into the bin.
    - When the robot's gripper is over the target bin and the robot's gripper is closed, the robot should drop the cube into the bin.