if check("the robot's gripper is not near the door lock"):
        robot.reach("to door lock")
    if check("the robot's gripper is near the door lock and the robot's gripper is not around the dial"):
        robot.grab("dial")
    if check("the robot's gripper is around the dial and the dial is not at the correct position"):
        robot.turn("the dial to the correct position")
    if check("the dial is at the correct position"):
        robot.release("the dial")