# Steps:
    #  1. Move gripper to the side of the handle
    #  2. Push down on the handle from the side
    # First, move the gripper to the side of the handle.
    if check("the robot's gripper is not to the side of the handle"):
        robot.move("gripper to side of handle")
    # Once the gripper is to the side of the handle, push down on the handle
    # from the side.
    if check("the robot's gripper is to the side of the handle"):
        robot.push("down on handle from side")