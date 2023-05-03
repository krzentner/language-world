
    if check("the robot's gripper is not near the handle and the robot's gripper is not almost vertically aligned with the handle"):
        robot.put("gripper above the handle")
    if check("the robot's gripper is near the handle and the robot's gripper is not almost vertically aligned with the handle"):
        robot.put("gripper almost vertically aligned with the handle")
    if check("the robot's gripper is almost vertically aligned with the handle"):
        robot.push("down on handle")