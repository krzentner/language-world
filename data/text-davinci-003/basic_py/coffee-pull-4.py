
    if check("the robot's gripper is not near the mug"):
        robot.grab("mug")
    if check("the robot's gripper is near the mug and the mug is not forward aligned with the robot's gripper"):
        robot.align("mug with robot")
    if check("the robot's gripper is near the mug and the mug is forward aligned with the robot's gripper"):
        robot.pull("mug to goal")