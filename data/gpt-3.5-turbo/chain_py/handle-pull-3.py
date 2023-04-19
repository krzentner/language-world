# Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Pull the handle up
    # First, put the gripper above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.put("gripper above handle")
    # Once the gripper is above the handle, grab on to the handle.
    if check("the robot's gripper is above the handle and the robot's gripper is not around the handle"):
        robot.grab("handle")
    # Now that we have the handle, pull it up.
    if check("the robot's gripper is around the handle"):
        robot.pull("handle up")