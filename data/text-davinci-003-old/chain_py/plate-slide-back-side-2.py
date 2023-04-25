
    # Steps:
    #  1. Put gripper above plate
    #  2. Drop gripper around plate
    #  3. Move plate back sideways
    # First, put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with plate"):
        robot.put("gripper above plate")
    # If the gripper isn't around the plate, put it around the plate.
    if check("the robot's gripper is not around plate and the robot's gripper is open"):
        robot.drop("gripper around plate")
    # If the gripper is near the plate and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near plate and the robot's gripper is open"):
        robot.close("gripper around plate")
    # We closed the gripper, and the plate is still near the gripper, so maybe
    # we grabbed it.
    # Try to move the plate back sideways.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is around plate and the robot's gripper is closed"):
        robot.slide("plate back sideways")