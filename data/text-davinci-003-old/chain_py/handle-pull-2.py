
    # Steps:
    #  1. Grab the handle
    #  2. Pull up on the handle
    # First, grab the handle.
    if check("the robot's gripper is not around handle"):
        robot.grab("handle")
    # Once the handle is grabbed, pull up on it.
    if check("the robot's gripper is around handle"):
        robot.pull("handle up")