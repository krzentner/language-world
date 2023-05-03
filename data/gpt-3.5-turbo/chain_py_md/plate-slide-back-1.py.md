# plate-slide-back: slide the plate back into the target location
def plate_slide_back(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Slide the plate back to the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.place("gripper above plate")
    # If the gripper isn't around the plate, put it around the plate.
    if check("the robot's gripper is not around plate and the robot's gripper is open"):
        robot.drop("gripper around plate")
    # If the gripper is near the plate and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near plate and the robot's gripper is open"):
        robot.close("gripper around plate")
    # We closed the gripper, and the plate should be near the gripper, so maybe we
    # grabbed it.
    # Try to slide the plate back to the target location.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above plate and the robot's gripper is closed"):
        robot.slide("plate back to target location")