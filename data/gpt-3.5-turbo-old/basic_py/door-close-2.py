if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is forward aligned with the door handle and the door is not fully closed"):
        robot.push("door closed")