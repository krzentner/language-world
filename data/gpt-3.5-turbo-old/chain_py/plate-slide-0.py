# Steps:
    #  1. Put the gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Slide the plate to the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.place("gripper above plate")
    # If the gripper isn't around the plate, grab it.
    if check("the robot's gripper is not around plate and the robot's gripper is open"):
        robot.grab("plate")
    # If the gripper is around the plate, slide the plate to the target location.
    if check("the robot's gripper is around plate and the plate is below the robot's gripper"):
        robot.slide("the plate to the target location")