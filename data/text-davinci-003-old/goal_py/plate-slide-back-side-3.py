
    # Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Line the plate up with the target
    #  4. Slide the plate back sideways into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # If the plate is below the gripper as seen from the side, line up the plate
    # with the gripper by closing the gripper.
    if check("the robot's gripper is not above the plate and the robot's gripper is open"):
        robot.move_gripper("above the plate", close_gripper=True)
    # If the gripper can grab the plate, grab it and then slide it back sideways
    # into the target location.
    if check("the robot's gripper is above the plate and the robot's gripper is closed"):
        robot.move_gripper("back of the target location