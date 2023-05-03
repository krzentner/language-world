
    if check("the robot's gripper is not near wall and the robot's gripper is not near reach target"):
        robot.reach("to wall")
    if check("the robot's gripper is near wall and the robot's gripper is not near reach target"):
        robot.reach("over wall")