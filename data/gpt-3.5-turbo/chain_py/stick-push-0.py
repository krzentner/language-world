# Steps:
    #  1. Put the stick's end near the thermos
    #  2. Push the thermos to the goal
    # We can use the robot's arm and stick to push the thermos to the goal.
    # First, position the stick's end near the thermos.
    if check("the stick's end is not near the thermos"):
        robot.move("stick near the thermos")
    # If the stick's end is near the thermos, we can push the thermos to the goal
    # using the stick.
    if check("the stick's end is near the thermos"):
        robot.push("thermos to the goal using the stick")