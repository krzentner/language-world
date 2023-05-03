
    if check("the robot's gripper is not above cube"):
        robot.pickup("cube")
    if check("the robot's gripper is not near target location"):
        robot.sweep("cube to the target location")