if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle and the gripper is around the handle"):
        robot.pull("drawer open")