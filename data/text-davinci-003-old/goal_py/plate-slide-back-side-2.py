
    # Steps:
    #  1. Put gripper left of the plate
    #  2. Grab the plate with the gripper
    #  3. Line the plate up with the target location
    #  4. Slide the plate back sideways
    # First, put the gripper left of the plate.
    if check("the robot's gripper is not left of the plate"):
        robot.move_gripper("left of the plate")
    # If the plate is right of the gripper, go back to putting the gripper left
    # of the plate.
    # Because the plate is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("plate is not right of the robot's gripper and plate is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the plate", close_gripper=True)
    # As long the gripper is still mostly around the plate and the plate isn't
    # lined up with the target location, line up the plate with the target
    # location.
    if check("the plate is not horizontally aligned with the target location"):
        robot.move_gripper("horizontally aligned with the target location")
    # If the plate is lined up with the target location to the side, insert it.
    if check("the robot's gripper is forward aligned with the plate and the plate is horizontally aligned with the target location"):
        robot.move_gripper("left of the plate")