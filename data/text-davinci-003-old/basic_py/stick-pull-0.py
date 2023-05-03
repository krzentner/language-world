
    if check("robot's gripper is not near the stick"):
        robot.grab("stick")
    if check("robot's gripper is near the stick and the stick is not near the thermos"):
        robot.place("stick near thermometer")
    if check("the thermos is near the stick"):
        robot.pull("stick towards goal")