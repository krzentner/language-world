
    # Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate
    #  3. Slide the plate back into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # If the plate isn't near the gripper, move the gripper down.
    if check("the robot's gripper is not near the plate and the robot's gripper is open"):
        robot.move_gripper("near the plate", close_gripper=True)
    # Once the gripper is above, around, and closed on the plate, we can slide
    # the plate back into the target location.
    if check("the robot's gripper is around the plate"):
        robot.move_gripper("above the target location")