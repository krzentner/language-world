
    if check("the robot's gripper is not forward aligned with the door handle"):
        robot.align("gripper to door handle")
    if check("the robot's gripper is forward aligned with the door handle and the robot's gripper is open"):
        robot.grab("dial")
    if check("the robot's gripper is around dial"):
        robot.turn("left")