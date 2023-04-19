if check("the robot's gripper is not almost vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is almost vertically aligned with the handle and the robot's gripper is open"):
        robot.grab("handle")
    if check("the robot's gripper is around the handle and the robot's gripper is near the base of the handle"):
        robot.pull("handle up")