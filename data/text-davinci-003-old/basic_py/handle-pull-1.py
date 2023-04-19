
    if check("the robot's gripper is not above handle"):
        robot.put("gripper above handle")
    if check("the handle is below the robot's gripper"):
        robot.pull("handle up")