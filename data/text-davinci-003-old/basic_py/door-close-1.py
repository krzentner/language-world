
    if check("the robot's gripper is not near the door handle"):
        robot.reach("to door handle")
    if check("the robot's gripper is almost vertically aligned with the door handle"):
        robot.push("door closed")