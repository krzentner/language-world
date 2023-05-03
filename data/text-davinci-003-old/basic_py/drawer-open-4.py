
    if check("the robot's gripper is not vertically aligned with drawer handle and the robot's gripper is below the drawer handle"):
        robot.move("gripper to right of drawer handle")
    if check("the robot's gripper is near the drawer handle"):
        robot.pull("away from the drawer")
    if check("the robot's gripper is in front of the drawer handle"):
        robot.pull("away harder from the drawer")