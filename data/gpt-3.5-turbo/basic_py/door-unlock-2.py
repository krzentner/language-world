if check("the robot's gripper is not near the door lock"):
        robot.reach("to door lock")
    if check("the robot's gripper is near the door lock and the robot's gripper is not around the dial"):
        robot.grab("dial")
    if check("the robot's gripper is around the dial and the dial is not turned to the correct direction"):
        robot.turn("dial to the correct direction")
    if check("the dial is turned to the correct direction and the door is not unlocked"):
        robot.push("dial to unlock the door")