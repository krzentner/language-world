if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    if check("the robot's gripper is above cube and the robot's gripper is closed and the target bin is not below the gripper"):
        robot.move("gripper above target bin")
    if check("the gripper is above the target bin and the cube is not inside the bin"):
        robot.place("cube into bin")