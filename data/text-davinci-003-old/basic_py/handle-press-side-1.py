
    if check("the robot's gripper is not horizontally aligned with the handle"):
        robot.align("gripper to handle")
    if check("the robot's gripper is horizontally aligned with the handle and the robot's gripper is not near the handle"):
        robot.put("gripper near handle")
    if check("the robot's gripper is near the handle"):
        robot.push("down on handle")