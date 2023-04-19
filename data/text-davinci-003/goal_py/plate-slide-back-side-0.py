
    # Steps:
    #  1. Put gripper roughly above the plate
    #  2. Slide the plate backwards
    # To slide the plate back, we first need to understand where it is
    # and how it can be moved.
    # If the gripper isn't at the plate, put it roughly above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # If the robot has the plate and is looking down on it, it should be able to
    # slide the plate backwards.
    # We don't need to be careful about the direction, since the plate is large
    # and we're just pushing it.
    if check("the robot's gripper is above the plate"):
        robot.move_gripper("near the target location")