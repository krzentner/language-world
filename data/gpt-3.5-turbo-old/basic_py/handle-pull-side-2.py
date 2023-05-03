    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the handle is not left of the robot's gripper and the handle is not forward aligned with the robot's gripper"):
        robot.grab("handle")
    if check("the robot's gripper is forward aligned with the handle"):
        robot.pull("up on handle")