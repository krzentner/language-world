
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.put("gripper above dial")
    if check("the robot's gripper is above dial and the robot's gripper is open"):
        robot.grab("dial")
    if check("the robot's gripper is around the dial"):
        robot.twist("to desired setting")