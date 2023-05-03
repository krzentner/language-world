if check("the robot's gripper is not near drawer handle"):
        robot.move("gripper to drawer handle")
    if check("the robot's gripper is near drawer handle"):
        robot.push("drawer closed")