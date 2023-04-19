
    # Steps:
    #  1. Put gripper above plate
    #  2. Grab plate with gripper
    #  3. Line plate up with target location
    #  4. Slide plate back sideways into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate", close_gripper=True)
    # If the plate isn't left of the gripper, put it back above the plate.
    if check("the robot's gripper is horizontally aligned with the target location"):
        robot.move_gripper("left of the plate")
    # If the plate is aligned with the target location, slide it back.
    if check("the robot's gripper is left of the plate"):
        robot.move_gripper("vertically aligned with the target location")