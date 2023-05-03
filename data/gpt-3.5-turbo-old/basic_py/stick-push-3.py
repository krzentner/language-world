if check("the robot's stick is not near the thermos and the stick is not touching the thermos"):
        robot.move("the stick above the thermos")
    if check("the stick is touching the thermos and the thermos is not near the target location"):
        robot.push("the thermos to the goal using the stick")