
    # Steps:
    #  1. Put gripper above plate
    #  2. Grab plate with the gripper
    #  3. Line up plate with target location
    #  4. Slide plate sideways into target location
    # First, put the gripper roughly above plate, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # If the gripper isn't around the plate, put it around the plate.
    if check("the robot's gripper is not around the plate and the robot's gripper is open"):
        robot.move_gripper("near the plate", close_gripper=True)
    # If the gripper is near the plate and open, maybe we can grab it by
    # closing the gripper.
    if check("the robot's gripper is above the plate and the robot's gripper is closed"):
        robot.move_gripper("horizontally aligned with the target location")
    # If the gripper is lined up with the target location, we can just slide
    # the plate into the target location.
    if check("the robot's gripper is horizontally aligned with the target location"):
        robot.move_gripper("right of the target location")