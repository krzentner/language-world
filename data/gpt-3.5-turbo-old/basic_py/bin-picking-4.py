if check("the cube is not in the robot's field of view"):
        robot.move("to get a view of the cube")
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is near the cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    if check("the robot's gripper is above the target bin and the robot's gripper is closed"):
        robot.place("cube in the bin")