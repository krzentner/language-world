if check("the robot's gripper is not near the door dial and the dial is not at the zero position"):
        robot.rotate("the gripper to reach the dial and turn it to zero")
    if check("the dial is at the zero position"):
        robot.rotate("the dial to unlock the door")