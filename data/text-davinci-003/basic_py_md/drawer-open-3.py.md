

If check("the robot's gripper is not near the drawer handle"):
    robot.grab("drawer handle")
if check("the robot's gripper is aligned with drawer handle"):
    robot.pull("drawer open")