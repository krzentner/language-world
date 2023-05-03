# Steps:
    #  1. Put gripper near the handle
    #  2. Grab the handle with the gripper
    #  3. Lift the handle up
    # First, put the gripper near the handle.
    if check("the robot's gripper is not near the handle"):
        robot.move("gripper to handle")
    # If the gripper isn't around the handle yet, try to grab it.
    if check("the robot's gripper is near the handle and the robot's gripper is not around the handle"):
        robot.grab("handle")
    # If the gripper is around the handle, lift it up.
    if check("the robot's gripper is around the handle"):
        robot.lift("handle up")