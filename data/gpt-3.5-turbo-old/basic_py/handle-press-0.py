if check("the robot's gripper is not above the handle"):
        robot.place("gripper above handle")
    if check("the robot's gripper is above handle and the robot's gripper is not around the handle"):
        robot.drop("gripper around handle")
    if check("the robot's gripper is around handle"):
        robot.push("down on handle")