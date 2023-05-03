
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    if check("the robot's gripper is not around the cube"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is closed around the cube and the robot's gripper is not near target bin"):
        robot.move("gripper towards goal")
    if check("the robot's gripper is near target bin"):
        robot.release("cube into bin")