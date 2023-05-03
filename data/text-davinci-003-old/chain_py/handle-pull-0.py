
    # Steps:
    #  1. Put gripper below handle
    #  2. Grab handle with gripper
    #  3. Pull handle up
    # First, put the gripper under the handle.
    if check("the robot's gripper is not below the handle"):
        robot.put("gripper below handle")
    # If the handle is left of the robot's gripper, we should move the gripper
    # near the handle to start grabbing it.
    if check("the handle is left of the robot's gripper and the robot's gripper is not near the handle"):
        robot.grab("handle")
    # Now that the gripper is roughly around the handle, pull it up.
    if check("the robot's gripper is around the handle"):
        robot.pull("handle up")