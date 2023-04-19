
    # Steps:
    #  1. Put gripper forward aligned with the plate
    #  2. Push the plate back
    # If the plate isn't forward aligned with the robot's gripper, move the
    # gripper until it is forward aligned with the plate.
    if check("the robot's gripper is not forward aligned with the plate"):
        robot.put("gripper forward aligned with the plate")
    # Now that the robot's gripper is forward aligned with the plate, slide it
    # back.
    if check("the robot's gripper is forward aligned with the plate"):
        robot.slide("plate to target location")