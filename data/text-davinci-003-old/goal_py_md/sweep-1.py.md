

Steps:
1. Put gripper above cube
2. Drop gripper around cube
3. Close gripper around cube
4. Move cube sideways to target location

First, put the gripper roughly above the cube, so that we don't bump it while trying to grab it.
if check("the robot's gripper is not above the cube"):
    robot.move_gripper("above the cube")

If the gripper isn't around the cube, put it around the cube.
if check("the robot's gripper is not around cube and the robot's gripper is open"):
    robot.move_gripper("near the cube", close_gripper=True)

If the gripper is near the cube and open, maybe we can grab it by closing the gripper.
if check("the robot's gripper is above cube and the robot's gripper is closed"):
    robot.move_gripper("near the target location")

Once the gripper is near the target location, we can move the cube sideways by moving the gripper.
if check("the robot's gripper is near the target location"):
    robot.move_gripper("horizontally aligned with the target location")