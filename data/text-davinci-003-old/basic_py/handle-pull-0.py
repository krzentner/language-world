
    if check("the robot's gripper is not near the handle"):
        robot.put("gripper near handle")
    if check("the robot's gripper is near the handle"):
        robot.pull("up handle")