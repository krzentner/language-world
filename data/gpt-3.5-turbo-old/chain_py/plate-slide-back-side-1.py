# Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Line the plate up with the target location
    #  4. Slide the plate backwards into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    # If the plate becomes left of the gripper, go back to putting the gripper
    # above the plate.
    # Because the plate is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("plate is not left of the robot's gripper and plate is not forward aligned with the robot's gripper"):
        robot.grab("plate")
    # As long the gripper is still mostly around the plate and the plate isn't lined up
    # with the target location, line up the plate with the target location.
    if check("the robot's gripper is forward aligned with the plate and the plate is not horizontally aligned with the target location"):
        robot.align("plate to target location")
    # If the plate is lined up with the target location to the back, slide it backwards.
    if check("plate is horizontally aligned with target location (back side)"):
        robot.slide("plate backwards into the target location")