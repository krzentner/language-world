
    # Steps:
    #  1. Put gripper above plate
    #  2. Push gripper into the top of the plate
    #  3. Slide the plate to the target location
    # First, put the gripper above the plate, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # If the gripper isn't around the plate, put it around the plate.
    if check("the robot's gripper is not around the plate and the robot's gripper is open"):
        robot.move_gripper("near the plate", close_gripper=True)
    # If the gripper is near the plate and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above plate and the robot's gripper is closed"):
        robot.move_gripper("above the target location")