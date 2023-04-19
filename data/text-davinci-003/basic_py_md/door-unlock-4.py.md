

If check("the robot's gripper is not near the dial and the robot's gripper is not horizontally aligned with the dial"):
    robot.put("gripper above the dial")
if check("the robot's gripper is horizontally aligned with the dial and the robot's gripper is not around the dial"):
    robot.grab("gripper around dial")
if check("the robot's gripper is near the dial and the robot's gripper is open"):
    robot.close("gripper around dial")
if check("the robot's gripper is around the dial"):
    robot.turn("dial to unlock")