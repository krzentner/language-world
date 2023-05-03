
    if check("the robot's gripper is not near the target location"):
        robot.move("gripper to the target location")
    if check("the robot's gripper is near the target location"):
        robot.reach("the target location")