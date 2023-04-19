
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is not around handle and the robot's gripper is open"):
        robot.drop("gripper around handle")
    if check("the robot's gripper is around handle and the robot's gripper is closed"):
        robot.pull("handle up")