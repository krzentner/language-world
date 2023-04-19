
    # Steps:
    #  1. Put gripper above the plate
    #  2. Drop gripper around the plate
    #  3. Line the plate up with the target from the side
    #  4. Slide the plate to the target
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with plate"):
        robot.move_gripper("vertically aligned with the plate", close_gripper=True)
    # Next, line up the plate from the side with the target.
    if check("the plate is not horizontally aligned with target"):
        robot.move_gripper("horizontally aligned with the target")
    # Finally, if the plate is aligned with the target, slide the plate sideways
    # until it is in the target location.
    if check("the plate is horizontally aligned with target"):
        robot.move_gripper("left of the target location")