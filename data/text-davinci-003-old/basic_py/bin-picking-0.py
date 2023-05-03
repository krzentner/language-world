
    if check("the robot's gripper is not near the cube"):
        robot.move("gripper above cube")
    if check("the robot's gripper is near the cube and the gripper is open"):
        robot.grab("the cube")
    if check("the robot's gripper is near the cube and the gripper is closed"):
        robot.move("gripper above target bin")
    if check("the robot's gripper is near target bin and the gripper is open"):
        robot.drop("cube in target bin")