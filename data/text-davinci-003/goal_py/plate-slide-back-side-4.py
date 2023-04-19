
    # Steps:
    #  1. Put gripper above plate
    #  2. Grab plate with gripper
    #  3. Move plate to target location
    #  4. Slide plate sideways into target location
    # We need to put the gripper roughly above the plate, so that we don't bump
    # it while trying to grab it.
    if check("the robot's gripper is not above plate"):
        robot.move_gripper("above plate", close_gripper=True)
    # Once the gripper is above the plate, we should be able to grab the plate
    # by lining up the gripper and the plate.
    if check("the robot's gripper is above plate and the robot's gripper is not around plate"):
        robot.move_gripper("around plate")
    # Now that the gripper has the plate, move the gripper until the plate is
    # near the target location.
    if check("the robot's gripper is around plate and the plate is not near the target location"):
        robot.move_gripper("near the target location")
    # Once the plate is near the target location, slide it sideways into the
    # target location.
    if check("the robot's gripper is near the target location and the plate is not horizontally aligned with the target location"):
        robot.move_gripper("horizontally aligned with the target location")