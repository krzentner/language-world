
    # Steps:
    #  1. Put the gripper in front of the plate
    #  2. Trap the plate with the gripper
    #  3. Line up the plate with the target location
    #  4. Slide the plate sideways into the target location
    # First, move the gripper in front of the plate to line up the gripper with
    # the plate.
    if check("the robot's gripper is not forward aligned with plate"):
        robot.move_gripper("forward aligned with the plate", close_gripper=True)
    # Once the gripper is in front of the plate, close the gripper to trap the
    # plate.
    if check("the robot's gripper is forward aligned with plate and the robot's gripper is not closed"):
        robot.move_gripper("right of the plate", close_gripper=True)
    # Now that the plate is trapped, line it up with the target location.
    if check("the robot's gripper is right of the plate and the plate is not horizontally aligned with target location"):
        robot.move_gripper("horizontally aligned with target location")
    # Now that the plate is lined up with the target location, slide the plate
    # into the target location.
    if check("the robot's gripper is horizontally aligned with target location"):
        robot.move_gripper("right of the target location")