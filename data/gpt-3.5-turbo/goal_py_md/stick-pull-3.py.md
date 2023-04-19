# stick-pull: use the stick to pull the thermos to the target location
# def stick_pull(robot):
    # Steps:
    #  1. Put the stick end close to the thermos and target
    #  2. Push the stick into the ground next to the thermos
    #  3. Pull the stick towards the target location, dragging the thermos
    # We first need to put the end of the stick close to the thermos and the target
    if check("the stick is not positioned close to the thermos and target"):
        robot.move_stick("close to the thermos and target")
    # If the end of the stick is positioned close to the thermos and target, push the stick into the ground next to the thermos
    if check("the stick end is not pushed into the ground next to the thermos"):
        robot.move_stick("pushed into the ground next to the thermos")
    # If the stick is pushed into the ground next to the thermos, pull the stick towards the target location, dragging the thermos
    if check("the stick end is pushed into the ground next to the thermos and the stick end is not near the target"):
        robot.move_stick("near the target", get_thermos=True)