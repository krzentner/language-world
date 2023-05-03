# Steps:
    #  1. Line up the hammer with the nail from above
    #  2. Move the hammer down to hit the nail
    #  3. Move the hammer up
    # We need to line up the hammer directly above the nail first.
    # Because the hammer is a long object, we'll check if it's aligned from the
    # front instead of around it.
    if check("the hammer is not above the nail and the hammer is not forward aligned with the nail"):
        robot.move("hammer above nail")
    # If the hammer is above the nail and not touching it, move it down to hit
    # the nail.
    if check("the hammer is above the nail and not touching it"):
        robot.push("hammer down onto nail")
    # If the hammer is touching the nail, we've hit it.
    # Move the hammer back up so we can do something else.
    if check("the hammer is touching the nail"):
        robot.pull("hammer up")