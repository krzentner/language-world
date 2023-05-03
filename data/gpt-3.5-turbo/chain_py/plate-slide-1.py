# Steps:
    #  1. Put gripper above plate
    #  2. Drop gripper around plate
    #  3. Close gripper around plate
    #  4. Slide plate to goal
    # First, put the gripper roughly above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    # If the gripper isn't around the plate, put it around the plate.
    if check("the robot's gripper is not around the plate and the robot's gripper is open"):
        robot.drop("gripper around plate")
    # If the gripper is near the plate and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near plate and the robot's gripper is open"):
        robot.close("gripper around plate")
    # We closed the gripper, and the plate is still near the gripper, so maybe we
    # grabbed it.
    # Try to slide the plate to the goal.
    if check("the robot's gripper is holding the plate"):
        robot.slide("plate to goal")