# plate-slide-side: slide the plate sideways into the target location
# def plate_slide_side(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Line the plate up with the target location
    #  4. Slide the plate sideways to the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # If the plate is not below the gripper, we need to move the gripper above
    # the plate.
    if check("the robot's gripper is not above plate"):
        robot.move_gripper("above the plate", close_gripper=True)
    # Once the gripper is above the plate, we can start sliding it.
    if check("the robot's gripper is near the plate"):
        robot.move_gripper("left of the target location")