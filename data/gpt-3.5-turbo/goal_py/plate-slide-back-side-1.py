# Steps:
    #  1. Put gripper on the plate
    #  2. Lift plate slightly
    #  3. Slide plate sideways back to target location
    # First, make sure the gripper is lined up with the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # If the gripper is lined up with the plate, move it down to grab the plate.
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not around the plate"):
        robot.move_gripper("around the plate")
    # Once the gripper is around the plate, lift it slightly to make sure it
    # doesn't scrape against the surface as we slide it.
    if check("the robot's gripper is around the plate"):
        robot.move_gripper("above the plate")
    # Finally, slide the plate back sideways to the target location.
    if check("the robot's gripper is above the target location"):
        robot.move_gripper("horizontally aligned with the target location")