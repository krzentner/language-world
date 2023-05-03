# Steps:
    #  1. Put gripper right of the handle
    #  2. Grab the handle with the gripper
    #  3. Pull the handle up from the side
    # First, put the gripper right of the handle.
    if check("the robot's gripper is not right of the handle"):
        robot.move("gripper to the right of the handle")
    # If the gripper is right of the handle, grab the handle.
    if check("the robot's gripper is right of the handle and the handle is not in the gripper"):
        robot.grab("the handle")
    # Once the gripper has grabbed the handle, start pulling up to open it.
    if check("the handle is in the gripper"):
        robot.pull("up on the handle")