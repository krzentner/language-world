if check("the robot's gripper is not near the door handle and the dial"):
        robot.move("gripper to door handle and dial")
    if check("the robot's gripper is around the dial and the door handle"):
        robot.turn("dial to unlock door")