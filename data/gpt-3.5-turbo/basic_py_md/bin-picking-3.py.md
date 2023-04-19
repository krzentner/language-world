# bin-picking: pick up the cube and place it in the target bin
# def bin_picking(robot):
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        if check("the robot's gripper is not above the target bin"):
            robot.place("gripper above target bin")
        if check("the robot's gripper is not around the target bin and the robot's gripper is closed"):
            robot.drop("gripper around target bin")
        if check("the robot's gripper is near the target bin and the robot's gripper is closed"):
            robot.drop("gripper open and drop cube into target bin")