
    if check("the robot's gripper is not above the cube"):
        robot.reach("above cube")
    if check("the robot's gripper is above the cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    if check("the robot's gripper is near the cube and the robot's gripper is closed"):
        robot.place("cube in target bin")