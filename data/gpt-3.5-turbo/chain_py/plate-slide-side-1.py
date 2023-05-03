# Steps:
    #  1. Put gripper above the plate
    #  2. Grab the plate with the gripper
    #  3. Line the plate up with the target location
    #  4. Slide the plate sideways into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    # If the gripper isn't around the plate, put it around the plate.
    if check("the robot's gripper is not around plate and the robot's gripper is open"):
        robot.drop("gripper around plate")
    # If the gripper is near the plate and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near plate and the robot's gripper is open"):
        robot.close("gripper around plate")
    # We closed the gripper, and the plate is still near the gripper, so maybe we
    # grabbed it.
    # Try to line up the plate with the target location.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above plate and the robot's gripper is closed and the plate is near the target"):
        robot.align("plate to target and the robot's gripper is closed")
    # If the plate is aligned with the target to the side, slide it in.
    if check("the plate is vertically aligned with the target and the plate is not forward aligned with the target and the robot's gripper is closed"):
        robot.slide("the plate sideways into the target location")