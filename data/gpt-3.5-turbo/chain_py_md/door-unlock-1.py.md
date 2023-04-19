# door-unlock: turn the dial on the door
# def door_unlock(robot):
    # Steps:
    #  1. Put gripper around the dial
    #  2. Turn the dial to the right to unlock
    # We need to put the gripper around the dial before we can turn it.
    if check("the robot's gripper is not around the dial"):
        robot.grab("dial")
    # If the dial is not turned to the right, we need to turn it.
    # We can't just turn the dial right away because it might already be at the
    # right position, so we'll have to first check by turning it left just a bit
    # and then seeing if turning it right works.
    if check("the dial is not turned to the right"):
        # Turn the dial a bit to the left
        robot.turn("the dial to the left a bit")
        # If the dial is now turned to the right, we're done
        if check("the dial is turned to the right"):
            return
        # If the dial isn't turned to the right, turn it farther to the right.
        robot.turn("the dial to the right")