
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is not near the handle"):
        robot.grab("handle")
    if check("the robot's gripper is near the handle"):
        robot.pull("up on handle")