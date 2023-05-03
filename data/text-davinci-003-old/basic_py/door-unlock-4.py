
    if check("the robot's gripper is not above the door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is slightly above the door handle"):  
        robot.grab("door handle")
    if check("door handle is in robot's gripper"):
        robot.turn("right")