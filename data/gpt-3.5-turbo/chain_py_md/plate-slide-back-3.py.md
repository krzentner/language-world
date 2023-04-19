# plate-slide-back: slide the plate back into the target location
# def plate_slide_back(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Drop gripper around the plate
    #  3. Slide the plate to the target location
    # First, put the gripper roughly above the plate so that it doesn't bump into
    # it while trying to grab it.
    if check("the robot's gripper is not above the plate"):
        robot.place("gripper above plate")
    # If the gripper isn't around the plate, put it around the plate.
    if check("the robot's gripper is not around the plate and the robot's gripper is open"):
        robot.drop("gripper around plate")
    # If the gripper is near the plate, we've probably trapped the plate and can
    # slide it back to the target location.
    # Move the gripper back to its starting location.
    if check("the robot's gripper is near the plate and the plate is above the robot's gripper"):
        robot.move("gripper back to starting location")
    # Slide the plate back to the target location.
    if check("the robot's gripper is at the starting location"):
        robot.slide("plate to target location")