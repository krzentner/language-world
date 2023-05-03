
    # Steps:
    #  1. Put gripper above the plate
    #  2. Align the plate with the goal
    #  3. Slide the plate to the goal
    # Put the gripper above the plate if it isn't there
    if check("the robot's gripper is not above plate"):
        robot.put("gripper above plate")
    # If the goal isn't aligned with the plate as viewed from the side, we should
    # try to align the plate.
    if check("the goal is not aligned with the plate"):
        robot.align("plate to goal")
    # If the plate and goal are aligned, we can now slide the plate to the goal.
    if check("the plate and goal are aligned"):
        robot.slide("plate back to goal")