
    # Steps:
    #  1. Put gripper around the drawer handle
    #  2. Pull open the drawer
    # First, put the gripper near the drawer handle.
    # We want to make sure we're lined up properly, because otherwise the drawer
    # might get jammed.
    if check("the robot's gripper is not horizontally aligned with drawer handle"):
        robot.put("gripper around drawer handle")
    # If the gripper is lined up with the handle, start pulling the drawer open.
    if check("the robot's gripper is horizontally aligned with drawer handle"):
        robot.pull("drawer open")