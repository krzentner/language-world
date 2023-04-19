
    if check("the robot's gripper is not above the plate"):
        robot.move('gripper above the plate')
    if check("the robot is close to the target and the robot's gripper is not near the plate"):
        robot.put('gripper to the plate')
    if check("the robot's gripper is near the plate and the plate is below the robot's gripper"):
        robot.slide('the plate to the goal')