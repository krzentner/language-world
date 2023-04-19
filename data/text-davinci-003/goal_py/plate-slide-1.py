
    # Steps:
    #  1. Put gripper above the plate
    #  2. Hold the plate with the gripper
    #  3. Slide the plate to the target location
    # First, put the gripper roughly above the plate so we don't bump it when
    # grabbing it.
    if check("the robot's gripper is not roughly above the plate"):
        robot.move_gripper("above the plate")
    # If the gripper isn't around the plate, put it around the plate.
    if check("the robot's gripper is not around the plate and the robot's gripper is open"):
        robot.move_gripper("near the plate", close_gripper=True)
    # If the plate is below the robot's gripper, close the gripper to hold the
    # plate and move the plate to the target location.
    if check("the robot's gripper is around the plate and the plate is below the robot's gripper"):
        robot.move_gripper("above the target location")