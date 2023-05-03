if check("the robot's gripper is not near the dial"):
        robot.move("gripper to dial")
    if check("the robot's gripper is near the dial and the robot's gripper is not around the dial"):
        robot.grab("dial")
    if check("the robot's gripper is around the dial and the robot's gripper is not vertically aligned with the dial"):
        robot.align("gripper with dial")
    if check("the robot's gripper is vertically aligned with the dial and the dial is not turned to the desired position"):
        robot.turn("the dial to desired position")
    if check("the dial is turned to the desired position"):
        robot.release("dial")