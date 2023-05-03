
    # Steps:
    #  1. Put gripper above the plate
    #  2. Drop gripper around the plate
    #  3. Slide the plate to the target location
    # We need to put the gripper at the top of the plate to slide it, so line up
    # the gripper and the plate from above.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # If the gripper isn't around the plate, move it around the plate.
    if check("the robot's gripper is not around plate"):
        robot.move_gripper("near the plate", close_gripper=True)
    # Now that the gripper is around the plate, slide the plate towards the
    # target location.
    if check("the plate is not near the target location"):
        robot.move_gripper("near the target location")