# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Line the plate up with the target location
    #  4. Slide the plate sideways into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    # If the plate is not in the gripper, grab it.
    if check("the plate is not in the robot's gripper"):
        robot.grab("plate")
    # If the plate is not aligned with the target location, align it.
    if check("the plate is not horizontally aligned with target location"):
        robot.align("plate to target")
    # If the plate is aligned with the target location, slide it sideways.
    if check("the plate is horizontally aligned with target location"):
        robot.slide("plate into target location")