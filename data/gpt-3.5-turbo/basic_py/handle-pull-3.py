if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not around handle"):
        robot.grab("handle")
    if check("the robot's gripper is around handle"):
        robot.pull("up on handle")