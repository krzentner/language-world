
    if check("door handle is not above the robot's gripper"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is above the door handle and the door handle is not near the robot's gripper"):
        robot.move("gripper to door handle")
    if check("the door handle is near the robot's gripper"):
        robot.push("door closed")