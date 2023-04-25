
    # Steps:
    #  1. Put the stick in front of the thermos
    #  2. Push the stick towards the thermos
    #  3. Slide the thermos to the target location
    # First, put the stick in front of the thermos.
    if check("the stick is not in front of the thermos"):
        robot.put("stick in front of thermos")
    # If the stick is in front of the thermos, we can start pushing.
    if check("the stick is in front of the thermos"):
        robot.push("stick towards thermos")
    # If the thermos is pushed close enough to the stick, we can slide it to the
    # target location.
    if check("the thermos is close enough to the stick"):
        robot.slide("thermos to target")