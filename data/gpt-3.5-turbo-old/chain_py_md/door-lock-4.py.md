# door-lock: turn the dial on the door
# def door_lock(robot):
    # Steps:
    #  1. Put gripper around the dial
    #  2. Turn the dial clockwise until it stops
    #  3. Turn the dial counterclockwise to the combination
    #  4. Turn the dial clockwise until it stops again to lock the door
    # First, put the gripper around the dial to begin turning it.
    if check("the robot's gripper is not around the dial and the robot's gripper is open"):
        robot.drop("gripper around the dial")
    # Turn the dial clockwise until it stops.
    # We know the direction to turn it because we need to turn it to the right to
    # unlock the door.
    if check("the robot's gripper is around the dial"):
        robot.turn("dial clockwise until it stops")
    # Turn the dial counterclockwise to the combination.
    # The amount to turn counterclockwise needs to be found experimentally, so
    # the robot needs to know the combination beforehand.
    if check("the robot's gripper is around the dial"):
        robot.turn("dial counterclockwise to combination")
    # Turn the dial clockwise until it stops to lock the door.
    if check("the robot's gripper is around the dial"):
        robot.turn("dial clockwise until it stops to lock door")