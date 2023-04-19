

If check("the robot's gripper is not above the dial"):
    robot.put("gripper above dial")
if check("the robot's gripper is above the dial and the robot's gripper is not around the dial"):
    robot.drop("gripper around dial")
if check("the robot's gripper is around the dial and the robot's gripper is open"):
    robot.close("gripper around dial")
if check("the robot's gripper is closed around the dial"):
    robot.turn("dial in desired direction")