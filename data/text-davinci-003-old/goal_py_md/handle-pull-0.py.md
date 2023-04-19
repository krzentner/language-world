

Steps:
1. Put gripper above the handle
2. Drop gripper around the handle
3. Pull up the handle

if check("the robot's gripper is not above the handle"):
    robot.move_gripper("above the handle")

if check("the robot's gripper is not around the handle and the robot's gripper is open"):
    robot.move_gripper("near the handle", close_gripper=True)

if check("the robot's gripper is above the handle and the robot's gripper is closed"):
    robot.move_gripper("upwards from the handle")