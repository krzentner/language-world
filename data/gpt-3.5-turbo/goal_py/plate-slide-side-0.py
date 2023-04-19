# Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Line the plate up with the target location
    #  4. Slide the plate sideways into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # If the plate becomes left of the gripper, go back to putting the gripper
    # above the plate.
    # Because the plate is a large object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("plate is not left of the robot's gripper and plate is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the plate", close_gripper=True)
    # As long the gripper is still mostly around the plate and the plate isn't
    # lined up with the target location, line up the plate with the target
    # location.
    if check("plate is horizontally aligned with target location"):
        robot.move_gripper("above the plate")
    # If the plate is lined up with the target location to the side, slide it
    # in.
    if check("the robot's gripper is forward aligned with the plate and the plate is not horizontally aligned with target location"):
        robot.move_gripper("horizontally aligned with target location")