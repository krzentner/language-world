
    if check("the robot's gripper is not near door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is near door handle and the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is around door handle"):
        robot.push("door closed")