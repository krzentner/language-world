
    # Steps:
    #  1. Put gripper in front of the plate
    #  2. Grab the plate
    #  3. Line up the plate with with the target location
    #  4. Slide the plate back
    # Place the gripper in front of the plate.
    if check("the robot's gripper is not in front of the plate"):
        robot.put("gripper in front of the plate")
    # If the gripper is in front of the plate, grab it.
    if check("the robot's gripper is in front of the plate and the robot's gripper is open"):
        robot.grab("plate")
    # As long as the plate isn't lined up with the target location, line it up.
    if check("the robot's gripper is holding the plate and the plate is not horizontally aligned with the goal"):
        robot.align("plate to goal")
    # If the plate is horizontally aligned with the goal, slide it back into the
    # goal.
    if check("the plate is horizontally aligned with the goal"):
        robot.slide("plate back to goal")