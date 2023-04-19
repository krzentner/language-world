
    if check("the robot's gripper is not above the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is above the handle and the robot's gripper is not near handle"):
        robot.grab("handle")
    if check("the robot's gripper is near the handle"):
        robot.pull("handle upwards")