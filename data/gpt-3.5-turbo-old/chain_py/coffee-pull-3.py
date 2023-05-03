# Steps:
    #  1. Put gripper around the mug handle
    #  2. Pull mug towards the target location
    # First, put the gripper around the mug handle.
    if check("the robot's gripper is not around the mug handle"):
        robot.grab("mug handle")
    # If the gripper is around the mug handle, we can just pull the mug towards
    # the target location.
    if check("the robot's gripper is around the mug handle and the mug is not at the target location"):
        robot.pull("mug towards the target location")