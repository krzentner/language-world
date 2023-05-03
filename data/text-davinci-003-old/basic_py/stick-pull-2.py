
    if check("the robot's gripper is not near the stick and the robot's gripper is not above the stick"):
        robot.grab("stick")
    if check("the robot's gripper is near the stick and the thermos is not near the stick"):
        robot.put("stick under thermos")
    if check("the thermos is near the stick"):
        robot.pull("the stick and thermos towards the goal")