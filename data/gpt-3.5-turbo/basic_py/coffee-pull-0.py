if check("the robot's gripper is not near the mug handle"):
        robot.grab("mug handle")
    if check("the robot's gripper is forward aligned with the mug handle"):
        robot.pull("mug to the target location")