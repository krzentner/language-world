if check("the robot's gripper is not vertically aligned with handle and the robot's gripper is below handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with handle and the handle is not in the up position"):
        robot.pull("handle up")