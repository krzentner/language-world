
    # Steps:
    #  1. Put gripper forward of handle
    #  2. Move gripper to the side
    #  3. Push down on handle
    # 
    # First, we should move the gripper forward of the handle.
    if check("the robot's gripper is not forward of handle"):
        robot.move("gripper forward of handle")
    # Move the gripper to the side.
    # We don't need to be precise, since the handle is large enough to occupy
    # the gripper.
    if check("the robot's gripper is forward of handle"):
        robot.move("gripper to the side")
    # If the gripper is to the side of the handle, push down on the handle.
    if check("the robot's gripper is to the side of the handle"):
        robot.push("down on the handle")