# Steps:
    #  1. Put gripper above plate
    #  2. Grab the plate with the gripper
    #  3. Slide the plate to the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    # Once the gripper is above the plate, grab the plate.
    if check("the robot's gripper is above the plate and the robot's gripper is open"):
        robot.grab("plate")
    # Now that we have the plate, slide it to the target location.
    if check("the robot's gripper is holding the plate and the plate is not at the target location"):
        robot.slide("plate to goal")