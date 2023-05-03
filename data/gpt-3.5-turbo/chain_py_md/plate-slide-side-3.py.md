# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    # Steps:
    #  1. Put gripper roughly near the plate
    #  2. Close the gripper around the plate
    #  3. Slide the plate sideways into the target location
    # First, put the gripper roughly near the plate.
    if check("the robot's gripper is not near the plate"):
        robot.place("gripper near plate")
    # Assuming the gripper is close enough to the plate, we can try to close the
    # gripper around the plate.
    if check("the robot's gripper is near the plate and the robot's gripper is open"):
        robot.grab("plate")
    # If the gripper is closed around the plate, we can slide the plate sidewards
    # into the target location.
    if check("the plate is in the robot's gripper"):
        robot.slide("plate sideways into target location")