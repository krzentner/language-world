
    # Steps:
    #  1. Put gripper below plate in the middle of the plate
    #  2. Grip the plate
    #  3. Slide the plate sideways
    # The plate is wide, so we can start by just grabbing it from below it.
    # We don't need to be careful about the angle or direction.
    if check("the robot's gripper is not below plate"):
        robot.move_gripper("below the plate", close_gripper=True)
    # If the plate is below the robot's gripper, try sliding it.
    if check("robot's gripper is below plate"):
        robot.move_gripper("above the target location")