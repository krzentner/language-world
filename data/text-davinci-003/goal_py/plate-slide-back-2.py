
    # Steps:
    #  1. Put gripper directly above the plate
    #  2. Push down on the plate to line up with the target spot
    #  3. Slide the plate into the target spot
    # First, put the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate", close_gripper=True)
    # The plate should be slidable if the gripper is already above it. The plate
    # can only slide if it is forward aligned with the target spot.
    # Slide the plate into the target spot.
    if check("the robot's gripper is above the plate and the plate is forward aligned with the target spot"):
        robot.move_gripper("left of the plate")