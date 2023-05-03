
    if check("the robot's gripper is not above the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not around handle"):
        robot.grab("handle")
    if check("the robot's gripper is around handle"):
        robot.push("down on handle")