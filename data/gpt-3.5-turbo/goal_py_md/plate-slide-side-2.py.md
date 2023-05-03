# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    # Steps:
    #  1. Line up gripper above the plate
    #  2. Grab the plate with gripper
    #  3. Slide the plate sideways to the target location
    # First, line up the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # Once the gripper is lined up, grab the plate by moving the gripper down.
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not around the plate"):
        robot.move_gripper("around the plate")
    # Once the gripper is around the plate, slide the plate sideways to the target location.
    if check("the robot's gripper is around the plate and the robot's gripper is not horizontally aligned with the target location"):
        robot.move_gripper("horizontally aligned with the target location")