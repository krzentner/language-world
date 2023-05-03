# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    # Steps:
    #  1. Position gripper near the plate
    #  2. Pinch plate from the side
    #  3. Slide plate towards the target location
    # First, position the gripper near to the plate
    if check("gripper is not near the plate"):
        robot.move_gripper("near the plate")
    # Once gripper is near the plate, pinch the plate from the side
    if check("gripper is near the plate but not pinched from side"):
        robot.move_gripper("pinched on the side of the plate")
    # After pinching the plate, slide it towards the target location
    if check("plate is not at target location"):
        robot.move_gripper("above the target location")