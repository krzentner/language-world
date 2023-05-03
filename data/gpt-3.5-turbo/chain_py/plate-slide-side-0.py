# Steps:
    #  1. Put gripper above plate
    #  2. Grab plate with the gripper
    #  3. Line plate up with target
    #  4. Slide the plate sideways towards target
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    # If the gripper isn't around the plate, put it around the plate.
    if check("the robot's gripper is not around plate and the robot's gripper is open"):
        robot.put("gripper around plate")
    # If the gripper is around the plate, line it up with the target
    if check("the robot's gripper is around plate and plate is not aligned with target"):
        robot.align("plate to target")
    # Once it has been aligned, slide the plate sideways towards target
    if check("plate is aligned with target"):
        robot.slide("plate to target")