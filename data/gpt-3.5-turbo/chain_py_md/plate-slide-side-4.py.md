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
    # Grab the plate with the gripper.
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is open"):
        robot.grab("plate")
    # Line up the gripper with the target location.
    if check("the robot's gripper is holding the plate and not aligned with the target location"):
        robot.align("plate to target location")
    # If the plate is aligned with the target location, slide it sideways into place.
    if check("the plate is horizontally aligned with the target location"):
        robot.slide("plate sideways into target location")