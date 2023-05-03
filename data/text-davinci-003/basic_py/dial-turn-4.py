
    if check("the robot's gripper is not above the dial"):
        robot.put("gripper above dial")
    if check("the robot's gripper is above the dial and the robot's gripper is not around the dial"):
        robot.grab("dial")
    if check("the robot's gripper is forward aligned with the dial"):
        robot.turn("dial until target is reached")
    if check("the target is reached"):
        robot.release("dial")