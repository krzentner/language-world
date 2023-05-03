

Steps:
1. Put gripper above the cube
2. Drop gripper around cube
3. Close gripper around cube
4. Move the cube to the target bin

if check("the robot's gripper is not above the cube"):
    robot.move_gripper("above the cube")

if check("the robot's gripper is not around cube"):
    robot.move_gripper("near the cube", close_gripper=True)

if check("the robot's gripper is above cube and the robot's gripper is closed"):
    robot.move_gripper("above the target bin")