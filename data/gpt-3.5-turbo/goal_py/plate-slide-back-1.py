# Steps:
    #  1. Put gripper above plate
    #  2. Grab the plate with the gripper
    #  3. Slide the plate back to the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # If the gripper is around the plate but not yet at the target location,
    # slide it back.
    # Because we're sliding the plate, it doesn't matter what direction we start
    # in, as long as we're over the plate.
    if check("the robot's gripper is around the plate and the plate is not horizontally aligned with the target location"):
        robot.move_gripper("horizontally aligned with the target location")