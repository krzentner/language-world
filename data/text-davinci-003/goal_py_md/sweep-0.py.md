

Steps:
1. Put gripper above cube
2. Drop gripper around cube
3. Close gripper around cube
4. Move cube sideways to goal

if check("the robot's gripper is not above cube"):
    robot.move_gripper("above the cube")
if check("the robot's gripper is not around the cube and the robot's gripper is open"):
    robot.move_gripper("near the cube", close_gripper=True)
if check("the robot's gripper is around cube and the robot's gripper is closed"):
    robot.move_gripper("right of the target location")