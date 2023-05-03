if check("the robot's gripper is not near the dial"):
        robot.move("gripper to the dial")
    if check("the dial is not aligned with the robot's gripper"):
        robot.align("dial with gripper")
    if check("the dial is aligned with the robot's gripper and the dial is not unlocked"):
        robot.turn("dial to the right")
    if check("the dial is unlocked"):
        print("door is now unlocked")