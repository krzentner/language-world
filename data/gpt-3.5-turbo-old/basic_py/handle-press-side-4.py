if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper next to handle")
    if check("the robot's gripper is next to the handle"):
        robot.push("down on handle")