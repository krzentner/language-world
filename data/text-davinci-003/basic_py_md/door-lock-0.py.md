

if check("the robot's gripper is not above the dial"):
    robot.put("gripper above dial")
if check("the robot's gripper is above the dial and the robot's gripper is open"):
    robot.drop("gripper around dial")
if check("the robot's gripper is around the dial and the robot's gripper is closed"):
    robot.turn("dial to the right to lock")