# Steps:
    #  1. Put gripper roughly around side of the plate
    #  2. Push the plate back into the target location
    # We don't need to be very precise with the placement of the gripper, since
    # we're just pushing the plate sideways.
    # If the gripper isn't around the plate, move it roughly to the side of the
    # plate.
    if check("the robot's gripper is not around the plate and the robot's gripper is not near the plate"):
        robot.put("gripper roughly around side of plate")
    # If the gripper is near the plate, we should be able to trap it.
    # Push the plate back into the target location.
    if check("the robot's gripper is near the plate"):
        robot.slide("plate back to target location")