# Steps:
    #  1. Put gripper above handle
    #  2. Grab handle
    #  3. Pull handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not above handle"):
        robot.put("gripper above handle")
    # If the gripper isn't around the handle, put it around the handle.
    if check("the robot's gripper is not around handle and the robot's gripper is open"):
        robot.grab("handle")
    # Once the gripper is around the handle, we can pull it.
    if check("the robot's gripper is around handle"):
        robot.pull("handle up")