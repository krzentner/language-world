

If check("the robot's gripper is not above the dial"):
    robot.put("gripper above dial")
if check("the robot's gripper is not around the dial and the gripper is open"):
    robot.drop("gripper around dial")
if check("the robot's gripper is around the dial and the gripper is open"):
    robot.close("gripper around dial")
if check("the robot's gripper is near the dial and the gripper is closed"):
    robot.turn("dial")