
    # Steps:
    #  1. Put the stick in front of the thermos
    #  2. Push the stick into the thermos
    #  3. Push the thermos to the target location
    # First, put the stick the thermos.
    # Because the thermos might be on a slant, the stick needs to be in front of
    # the thermos.
    if check("the stick is not near thermos"):
        robot.place("stick in front of thermos")
    # If the stick isn't pushing against the thermos, reposition the stick
    # roughly above the thermos and then push it into the thermos.
    if check("the stick is not pushing against the thermos"):
        robot.push("stick into thermos")
    # Now that the stick is pushing against the thermos, push the thermos to the
    # target location.
    if check("the stick is pushing against the thermos"):
        robot.push("thermos to goal")