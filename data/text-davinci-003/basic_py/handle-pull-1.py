
    if check("the robot's gripper is not above handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is above handle and the robot's gripper is open"):
        robot.grab("handle")
    if check("the robot's gripper is above handle and the robot's gripper is closed"):
        robot.pull("handle up")