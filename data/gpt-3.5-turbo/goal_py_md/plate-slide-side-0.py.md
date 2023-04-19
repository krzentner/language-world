# plate-slide-side: slide the plate sideways into the target location
# def plate_slide_side(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Position the gripper over the target location
    #  4. Slide the plate sideways into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # If the plate is not close to the gripper, move the gripper close to the plate.
    if check("the robot's gripper is not close to the plate and the robot's gripper is open"):
        robot.move_gripper("above the plate", close_gripper=True)
    # If the gripper is around the plate and not over the target location, move it over the target location.
    if check("the robot's gripper is near the plate and the plate is not below the robot's gripper"):
        robot.move_gripper("over the target location")
    # If the gripper is over the target location, slide the plate sideways.
    if check("the robot's gripper is almost horizontally aligned with the plate and the plate is below the robot's gripper"):
        robot.move_gripper("over the target location and horizontally aligned with the plate")