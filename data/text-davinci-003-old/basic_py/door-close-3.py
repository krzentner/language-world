
    if check("the robot's gripper is not near the door handle"):
        robot.put("gripper near door handle")
    if check("the robot's gripper is near the door handle"):
        robot.push("door closed")