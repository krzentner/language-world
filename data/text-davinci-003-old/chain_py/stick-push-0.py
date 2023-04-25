
    # Steps:
    #  1. Orient the stick
    #  2. Push the stick against the thermos
    #  3. Move the thermos
    # First, orient the stick.
    if check("the stick is not oriented correctly"):
        robot.orient("stick")
    # Once the stick is oriented, we can push the stick against the thermos.
    if check("the stick is oriented correctly"):
        robot.push("stick against thermos")
    # Once the stick is pushing against the thermos, move the thermos to the
    # target location.
    if check("the stick is pushing against the thermos"):
        robot.move("thermos to goal")