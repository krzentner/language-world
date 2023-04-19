if check("the robot's stick is not touching the thermos"):
        robot.move("stick to touch thermos")
    if check("the thermos is not near the goal location"):
        robot.pull("thermos towards goal")
    if check("the thermos is near the goal location"):
        robot.move("stick away from thermos")