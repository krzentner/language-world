
    if check("the robot's gripper is not almost vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is almost vertical to handle and the robot's gripper is not around handle"):
        robot.grab("handle")
    if check("the robot's gripper is around the handle"):
        robot.pull("up on handle")