
    if check("the robot's gripper is not vertically aligned with the window handle"):
        robot.put("gripper above the window handle")
    if check("the robot's gripper is above the window handle and the robot's gripper is not near the window handle"):
        robot.put("gripper to left of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window right")
    if check("the robot's gripper is right of the window handle"):
        robot.push("window right harder")