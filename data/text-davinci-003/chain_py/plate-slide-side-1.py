
    # Steps:
    #  1. Put gripper above the plate
    #  2. Drop gripper around the plate from the side
    #  3. Slide the plate sideways
    # Put the gripper above the plate. We want to do this from the side, so it
    # catches the edge of the plate.
    if check("the robot's gripper is not horizontally aligned with the plate"):
        robot.put("gripper above the plate from the side")
    # If the gripper is lined up with the plate from the side, move it down to
    # catch the edge.
    if check("the robot's gripper is horizontally aligned with the plate and the robot's gripper is open"):
        robot.put("gripper around the plate from the side")
    # If the gripper is near the plate and open, close it to trap the plate so
    # we can slide it.
    if check("the robot's gripper is near the plate and the robot's gripper is open"):
        robot.close("gripper around the plate")
    # If the gripper is closed and the plate is not aligned with the goal,
    # slide the plate until it is.
    if check("the robot's gripper is closed around the plate and the plate is not aligned with the goal"):
        robot.slide("plate to the goal")