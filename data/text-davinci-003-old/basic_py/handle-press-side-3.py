
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is not aligned with the handle and the robot's gripper is not around the handle"):
        robot.put("gripper around handle")
    if check("the robot's gripper is around the handle"):
        robot.push("down on handle")