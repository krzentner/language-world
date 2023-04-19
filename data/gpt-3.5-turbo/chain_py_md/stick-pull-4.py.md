# stick-pull: use the stick to pull the thermos to the target location
# def stick_pull(robot):
    # Steps:
    #  1. Position the stick to grip the thermos from the top
    #  2. Grip the thermos with the stick
    #  3. Pull the thermos towards the target location using the stick
    # We need to position the stick so we can grip the thermos from the top. Move
    # the stick to the left of the thermos and above it.
    if check("the stick is not above and to the left of the thermos"):
        robot.move("stick to the left of the thermos")
        robot.move("stick above the thermos")
    # Once the stick is above and to the left of the thermos, grip it with the
    # stick.
    if check("the stick is positioned correctly and the stick is not gripping the thermos"):
        robot.grip("stick the top of the thermos")
    # Now we can pull the thermos towards the target location. Begin by moving
    # the stick towards the target location.
    if check("the thermos is not near the target location"):
        robot.move("stick towards the target location")
    # If the thermos isn't near the target location, we probably aren't gripping
    # it very tightly, so we should grip it even harder.
    if check("the thermos is still not near the target location"):
        robot.grip("tighter around the thermos")
        robot.move("stick towards the target location")
    # Keep moving the stick towards the target location and gripping the thermos
    # until it reaches the target location.
    while check("the thermos is still not at the target location"):
        robot.move("stick towards the target location")
        robot.grip("tighter around the thermos")