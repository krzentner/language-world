if check("the robot's gripper is not near the handle"):
        robot.put("gripper to the side of the handle")
    if check("the robot's gripper is aligned with the handle"):
        robot.push("down on the handle")