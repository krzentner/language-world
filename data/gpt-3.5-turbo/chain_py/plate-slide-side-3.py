# Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Line the plate up with the target location
    #  4. Slide the plate sideways into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    # If the gripper is not around the plate, grab the plate with the gripper.
    if check("the robot's gripper is not around plate and the robot's gripper is open"):
        robot.drop("gripper around plate")
        robot.close("gripper around plate")
    # If the gripper is near the plate and holding it, line up the plate with the
    # target location to slide it into place.
    if check("the robot's gripper is near plate and the robot's gripper is closed"):
        robot.align("plate to target location")
    # Once the plate is lined up with the target location, slide it into place
    # sideways
    if check("plate is horizontally aligned with target location"):
        robot.slide("plate sideways into target location")