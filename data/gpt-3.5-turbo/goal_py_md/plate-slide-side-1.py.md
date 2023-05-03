# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    # Steps:
    #  1. Position gripper above the plate
    #  2. Close the gripper around the plate
    #  3. Move the gripper sideways to slide the plate to the target location
    # Put the gripper above the plate, centered on it.
    if check("the robot's gripper is not vertically aligned with plate"):
        robot.move_gripper("vertically aligned with the plate")
    # Position the gripper to be around the plate's middle
    # and close the gripper.
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not around the plate"):
        robot.move_gripper("around the middle of the plate", close_gripper=True)
    # Slide the plate to the target location.
    if check("the robot's gripper is around the plate and the plate is not horizontally aligned with the target"):
        robot.move_gripper("horizontally aligned with the target")