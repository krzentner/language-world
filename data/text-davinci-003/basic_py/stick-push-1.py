
    if check("the robot's stick is not near the thermos"):
        robot.put("stick near thermos")
    if check("the robot's stick is near the thermos"):
        robot.apply("force with stick to move thermos")
    if check("the robot's stick is still not near the goal"):
        robot.slide("the thermos to the goal")