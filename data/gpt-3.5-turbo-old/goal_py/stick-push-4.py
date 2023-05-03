# Steps:
    #  1. Put the end of the stick near the thermos
    #  2. Push the thermos towards the target location
    # We can use the stick to push the thermos by moving the end of the stick
    # towards the thermos and then pushing it.
    if check("the end of the stick is not near the thermos"):
        robot.move_stick("near the thermos")
    # If the end of the stick is near the thermos, push the thermos towards the
    # target location using the stick.
    if check("the end of the stick is near the thermos"):
        robot.move_stick("near the target location")