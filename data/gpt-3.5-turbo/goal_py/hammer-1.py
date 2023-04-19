# Steps:
    #  1. Put the hammer head above the nail
    #  2. Move the hammer down to hit the nail
    # First, we need to position the hammer head above the nail.
    if check("the hammer head is not above the nail"):
        robot.move_hammer("above the nail")
    # Once the hammer head is positioned above the nail, we can move the
    # hammer down to hit it.
    if check("the hammer head is above the nail"):
        robot.move_hammer("onto the nail")