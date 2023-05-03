# Steps:
    #  1. Put gripper above plate
    #  2. Grab plate with gripper
    #  3. Line up the plate with the target location
    #  4. Slide the plate toward the target location
    # First, put the gripper roughly above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # If the gripper isn't around the plate, put it around the plate.
    if check("the robot's gripper is not around plate and the robot's gripper is open"):
        robot.move_gripper("near the plate", close_gripper=True)
    # If the gripper is around the plate, but the plate isn't aligned with the
    # target location yet, line it up.
    if check("the robot's gripper is around the plate and the plate is not aligned with the target location"):
        robot.move_gripper("aligned with the target location")
    # If the gripper is around the plate and the plate is aligned with the
    # target location, slide it toward the target location.
    if check("the robot's gripper is aligned with the target location and the plate is not near the target location"):
        robot.move_gripper("near the target location")