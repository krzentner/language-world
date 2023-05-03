
    if check(" the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is near door handle and the robot's gripper is not open"):
        robot.open("gripper around door handle")
    if check("the robot's gripper is open and near door handle"):
        robot.pull("away from door")