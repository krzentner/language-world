
    # Steps:
    #  1. Put gripper in front of plate
    #  2. Push plate straight ahead
    #  3. Slide plate sideways
    # To have the most control, we should line the robot's gripper up with the
    # plate horizontally first.
    if check("the robot's gripper is not forward aligned with the plate"):
        robot.move_gripper("forward aligned with the plate")
    # Now that the robot's gripper is aligned with the plate, we should push the
    # plate a bit forward, so that it's lined up with the target location
    # horizontally.
    if check("the plate is forward aligned with the target location"):
        robot.move_gripper("left of the plate")
    # If the plate is forward aligned with the target location, we can start
    # pushing it sideways
    if check("the plate is not forward aligned with the target location"):
        robot.move_gripper("above the target location")