# Steps:
    #  1. Put one end of the stick near the thermos
    #  2. Use the stick to hook onto the handle of the thermos
    #  3. Pull the stick back towards the target location, dragging the thermos
    # First, put one end of the stick close to the thermos.
    if check("one end of the stick is not near the thermos"):
        robot.move("one end of the stick close to the thermos")
    # Once the stick is close enough, use the other end of the stick to hook onto
    # the handle of the thermos.
    if check("one end of the stick is near the thermos but the stick is not hooked onto the thermos handle"):
        robot.hook("the stick onto the thermos handle")
    # With the stick hooked on, pull the stick back towards the target location
    # to drag the thermos.
    if check("the stick is hooked onto the thermos handle"):
        robot.pull("the stick back towards the target location, dragging the thermos")