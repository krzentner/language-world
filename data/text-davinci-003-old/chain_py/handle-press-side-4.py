
    # Steps:
    #  1. Put gripper roughly above the handle
    #  2. Move the gripper right so that it is lined up with the handle
    #  3. Push down on the handle
    # First, we need to put the activator roughly above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.put("gripper above handle")
    # If the gripper is currently above the handle, line it up with the handle.
    if check("the robot's gripper is above the handle and the robot's gripper is not right of the handle"):
        robot.align("gripper with handle")
    # When it's lined up, push down on the handle.
    if check("the robot's gripper is right of the handle"):
        robot.push("down on handle")