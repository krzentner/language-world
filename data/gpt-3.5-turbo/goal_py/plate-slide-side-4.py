# Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Slide the plate sideways to the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # As long as the gripper isn't around the plate, move it down to grab the
    # plate.
    if check("the robot's gripper is not around plate"):
        robot.move_gripper("around the plate", close_gripper=True)
    # If the gripper is around the plate, slide it horizontally towards the
    # target location.
    if check("the robot's gripper is around the plate"):
        robot.move_gripper("horizontally aligned with the target location")