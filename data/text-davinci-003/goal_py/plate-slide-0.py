
    # Steps:
    #  1. Put gripper above the plate
    #  2. Trap the plate by pushing down on it
    #  3. Slide the plate to the target location
    # First, the gripper should be put above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # With the gripper above the plate, close the gripper to trap the plate by
    # pushing down on it.
    if check("the robot's gripper is vertically aligned with the plate"):
        robot.move_gripper("above the plate", close_gripper=True)
    # After trapping the plate, slide the plate to the target location.
    if check("the robot's gripper is around the plate"):
        robot.move_gripper("near the target location")