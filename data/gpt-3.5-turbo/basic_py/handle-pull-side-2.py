if check("the robot's gripper is not vertically aligned with handle and the robot's gripper is not near handle"):
        robot.put("gripper near handle")
    if check("the robot's gripper is not around handle and the robot's gripper is open"):
        robot.grab("handle")
    if check("the robot's gripper is around handle and the handle is not pulled up"):
        robot.pull("handle up")