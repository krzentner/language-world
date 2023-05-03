if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is not around handle"):
        robot.grab("handle")
    if check("the robot's gripper is not behind the handle"):
        robot.move("gripper behind handle")
    if check("the robot's gripper is behind the handle and the handle is not pulled up"):
        robot.pull("handle up")