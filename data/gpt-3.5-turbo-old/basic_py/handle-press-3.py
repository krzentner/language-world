if check("the robot's gripper is not above the handle"):
        robot.lift("gripper above handle")
    if check("the robot's gripper is above the handle"):
        robot.push("down on handle")