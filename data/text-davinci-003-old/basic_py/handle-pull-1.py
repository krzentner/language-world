
    if check("the robot's gripper is not above handle"):
        robot.place("above handle")
    if check("the robot's gripper is closed and above handle"):
        robot.pull("handle up")