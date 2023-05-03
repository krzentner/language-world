# Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Pull the handle up
    # First, put the gripper above the handle
    if check("the robot's gripper is not above the handle"):
        robot.put("gripper above handle")
    # If the gripper is above the handle, grab the handle with the gripper
    if check("the robot's gripper is above the handle and the gripper is open"):
        robot.grab("handle")
    # Once the handle is grabbed, we can pull it up
    if check("the robot's gripper is around the handle"):
        robot.pull("handle up")