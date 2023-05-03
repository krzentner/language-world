

# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    # Steps:
    #  1. Put the gripper above the plate
    #  2. Slide the plate sideways into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # Once the gripper is lined up with the plate, slide it to the target
    if check("the robot's gripper is vertically aligned with the plate"):
        robot.move_gripper("horizontally aligned with the target location")