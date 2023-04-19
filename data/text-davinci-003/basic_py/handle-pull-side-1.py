
    if check("the robot's gripper is below handle and the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not near handle"):
        robot.push("gripper into handle")
    if check("the robot's gripper is near handle"):
        robot.pull("handle up")