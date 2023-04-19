
    # Steps:
    #  1. Place the stick in front of the thermos
    #  2. Push the thermos with the stick
    #  3. Pull the stick toward the goal
    # If the robot does not have the stick, pick it up off the ground.
    if check("the robot does not have the stick"):
        robot.grab("stick")
    # If the stick is not lined up with the thermos, place the stick in front of
    # the thermos.
    if check("the stick is not lined up with the thermos"):
        robot.place("stick in front of the thermos")
    # If the robot has the stick and the thermos is now in front of the stick,
    # start pushing.
    if check("the stick is lined up with the thermos and the thermos is in front of the stick"):
        robot.push("the thermos with the stick")
    # If the thermos is still in front of the stick, pull the stick toward the
    # goal.
    if check("the thermos is still in front of the stick"):
        robot.pull("stick towards the goal")