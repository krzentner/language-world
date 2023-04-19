
    # Steps:
    #  1. Put gripper around the handle
    #  2. Pull the handle up
    # We need to change the robot's gripper's position before it can grab the
    # handle.
    if check("the robot's gripper is not around the handle"):
        robot.grab("handle")
    # Once the robot has the handle, it can pull up on it.
    if check("the robot's gripper is around the handle"):
        robot.pull("handle up")