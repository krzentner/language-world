if check("the robot's gripper is not near the door handle"):
        robot.push("door closed")
    else:
        robot.grab("door handle")
        robot.push("door closed")