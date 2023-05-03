
    # Steps:
    #  1. Put gripper above the plate
    #  2. Drop gripper around the plate
    #  3. Slide the plate back sideways
    # First, put the gripper roughly above the plate, so that we don't damage the
    # plate while trying to grab it.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate", close_gripper=True)
    # If the gripper isn't around the plate, put it around the plate.
    if check("the robot's gripper is not around plate"):
        robot.move_gripper("left of the plate")
    # If the plate is left of the robot's gripper and the robot's gripper isn't
    # around the plate, slide the plate back.
    if check("the robot's gripper is left of the plate and the robot's gripper is not above the plate and the robot's gripper is not horizontally aligned with the plate"):
        robot.move_gripper("horizontally aligned with the plate")
    # finally, slide it to the target location.
    if check("the robot's gripper is horizontally aligned with the plate"):
        robot.move_gripper("above the target location")