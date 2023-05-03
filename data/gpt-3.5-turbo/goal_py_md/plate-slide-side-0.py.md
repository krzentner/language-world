# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    # Steps:
    #  1. Position gripper above plate
    #  2. Grab the plate with the gripper
    #  3. Tilt the plate to the side
    #  4. Slide the plate to the target location
    # First, position the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # Then, grab the plate with the gripper.
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not around plate"):
        robot.move_gripper("around the plate")
    # Next, tilt the plate to the side so it can be slid into the target location.
    if check("the plate is not tilted to the side"):
        robot.tilt_object("the plate", direction="side")
    # Finally, slide the plate into the target location.
    if check("the plate is tilted to the side and the robot's gripper is forward aligned with the target location"):
        robot.move_gripper("left of the target location")