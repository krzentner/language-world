
    if check("the robot's gripper is not vertically aligned with the hammer handle"):
        robot.put("gripper above hammer handle")
    if check("the robot's gripper is vertically aligned with the hammer handle and the robot's gripper is not above nail"):
        robot.grab("hammer handle")
    if check("the robot's gripper is vertically aligned with nail"):
        robot.strike("hammer into nail")