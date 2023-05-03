
    # Steps:
    #  1. Put gripper above the plate
    #  2. Drop gripper onto the plate
    #  3. Slide the plate
    # First, we should put the gripper above the plate, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above plate"):
        robot.move_gripper("above plate")
    # After the gripper is aligned with the plate, it should be able to grab it
    # by dropping down.
    if check("the robot's gripper is above plate and the robot's gripper is not around plate"):
        robot.move_gripper("around plate")
    # If the plate is not in the target location, we can now slide it over by
    # moving the gripper to the target location.
    if check("the robot's gripper is around the plate"):
        robot.move_gripper("near the target location")