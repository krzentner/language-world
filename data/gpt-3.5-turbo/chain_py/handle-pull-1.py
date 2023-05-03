# Steps:
    #  1. Grab the handle
    #  2. Pull the handle upwards
    # First, put the gripper around the handle.
    if check("the robot's gripper is not around the handle"):
        robot.grab("handle")
    # Once the gripper is around the handle, pull it up.
    if check("the robot's gripper is around the handle"):
        robot.pull("handle upwards")