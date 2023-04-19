
    # Steps:
    #  1. Put gripper near the plate
    #  2. Start sliding the plate into the target location
    #  3. Slide the plate slower as it approaches the target location
    # If the robot's gripper isn't near the plate, move it near the plate.
    if check("the robot's gripper is not near the plate"):
        robot.move_gripper("near the plate", close_gripper=True)
    # Start sliding the plate onto the target location.
    if check("the robot's gripper is near the plate"):
        robot.move_gripper("near the target location")
    # Once the plate is near the target location, slow down the movement to
    # reduce chance of knocking the plate off the target location.
    if check("the plate is close to the target location"):
        robot.move_gripper("slowly towards the target location")