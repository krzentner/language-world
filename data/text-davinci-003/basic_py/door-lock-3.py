
    if check("the robot's gripper is not near the dial"):
        robot.put("gripper near dial")
    if check("the robot's gripper is near the dial"):
        robot.rotate("dial to left or right")