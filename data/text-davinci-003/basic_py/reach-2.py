
    if check("the robot's arm is not close to target"):
        robot.move("robot's arm close to target")
    if check("the robot's arm is not pointed to target"):
        robot.turn("robot's arm to target")
    if check("the target is not within reach of the robot's gripper"):
        robot.extend("robot's arm to target")