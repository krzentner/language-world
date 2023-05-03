# Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Line the plate up with the target location
    #  4. Slide the plate into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # If the plate isn't trapped by the gripper, move the gripper down to grab it.
    if check("the robot's gripper is above the plate and the robot's gripper is not around the plate"):
        robot.move_gripper("around the plate", close_gripper=True)
    # Once the plate is held by the gripper, line it up with the target location.
    if check("the robot's gripper is around the plate and the plate is not horizontally aligned with the target location"):
        robot.move_gripper("horizontally aligned with the target location")
    # Finally, slide the plate into the target location.
    if check("the robot's gripper is horizontally aligned with the target location and the plate is not at the target location"):
        robot.move_gripper("near the target location", close_gripper=True)