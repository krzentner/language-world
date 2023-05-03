
    if check("the robot's gripper is not near the stick"):
        robot.reach("gripper to stick")
    if check("the robot's gripper is near the stick and the robot's gripper is open"):
        robot.drop("gripper around stick")
    if check("the robot's gripper is near the stick and the robot's gripper is closed"):
        robot.pull("thrmos with stick")