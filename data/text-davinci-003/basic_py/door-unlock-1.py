
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is near the door handle and the robot's gripper is not vertically aligned with dial"):
        robot.align("gripper to dial")
    if check("the robot's gripper is vertically aligned with dial"):
        robot.turn("dial to unlock")