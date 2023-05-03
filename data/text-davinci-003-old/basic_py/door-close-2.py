
    if check("the robot's gripper is not vertically aligned with the door handle and the robot's gripper is not near the door handle"):
        robot.put("gripper near door handle")
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.push("door close")