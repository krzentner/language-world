
    if check("the robot's gripper is not above the handle"):
        robot.place("gripper above handle")
    if check("the robot's gripper is above the handle and the robot's gripper is open"):
        robot.drop("gripper around handle")
    if check("the robot's gripper is around the handle and the robot's gripper is closed"):
        robot.pull("up on handle")