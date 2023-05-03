
    if check("the robot's gripper is not near the stick"):
        robot.grab("stick")
    if check("the robot's gripper is around stick"):
        robot.pull("stick towards thermos")
    if check("the robot's gripper is in front of thermos"):
        robot.push("stick towards thermos")