
    if check("robot's gripper is not near the stick and the stick is not near the thermos"):
        robot.grab("stick")
    if check("robot's gripper is near the stick and stick is not near the thermos"):
        robot.move("stick to the thermos")
    if check("the stick is near the thermos and thermos is not below the stick"):
        robot.put("stick below the thermos")
    if check("the stick is below thermos"):
        robot.pull("stick to the goal")