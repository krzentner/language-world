if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        if check("the target bin is left of the robot's gripper"):
            robot.move("gripper to the left of bin")
        if check("the target bin is in front of the robot's gripper"):
            robot.move("gripper to the front of bin")
        if check("the robot's gripper is above the target bin"):
            robot.drop("cube into bin")