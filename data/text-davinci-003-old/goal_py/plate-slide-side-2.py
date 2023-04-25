
    # Steps:
    #  1. Put gripper above the plate
    #  2. Drop gripper around the plate
    #  3. Slide the plate sideways into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate", close_gripper=True)
    # If the gripper is above the plate but not around it, move the gripper
    # around it.
    if check("the robot's gripper is above the plate and the robot's gripper is not around the plate"):
        robot.move_gripper("around the plate")
    # If the gripper is around the plate, we can slide it to the target
    # location.
    if check("the robot's gripper is around the plate"):
        robot.move_gripper("above the target location")