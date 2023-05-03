if check("the robot's gripper is not near the handle"):
        robot.put("gripper to the side of handle")
    if check("the robot's gripper is near the handle"):
        robot.push("down on handle from the side")