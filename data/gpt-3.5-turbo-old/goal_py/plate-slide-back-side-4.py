# Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Move gripper back until the plate is over the target location
    #  4. Slide the plate sideways into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # If the plate is not within the gripper and the gripper is open, grab the
    # plate with the gripper.
    if check("the robot's gripper is above the plate and the robot's gripper is open"):
        robot.move_gripper("near the plate", close_gripper=True)
    # Now that the plate is grabbed by the gripper, move the gripper back until
    # the plate is over the target location.
    if check("the robot's gripper is not over the target location"):
        robot.move_gripper("over the target location")
    # If the gripper is over the target location but not horizontally lined up
    # with it, move it horizontally into place.
    if check("the robot's gripper is over the target location and the plate is not horizontally aligned with the target location"):
        robot.move_gripper("horizontally aligned with the target location")