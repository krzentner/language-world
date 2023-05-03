
    if check("the robot's gripper is not near the cube"):
        robot.reach("cube")
    if check("the robot's gripper is above the cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    if check("the robot's gripper is near cube and the robot's gripper is closed"):
        robot.move("cube to the target bin")
    if check("the cube is in front of the target bin"):
        robot.place("cube in the target bin")