

If check("the robot's gripper is not below the dial"):
    robot.grab("dial")
if check("the robot's gripper is near the dial and the robot's gripper is open"):
    robot.close("gripper around dial")
if check("the robot's gripper is closed"):
    robot.turn("dial")