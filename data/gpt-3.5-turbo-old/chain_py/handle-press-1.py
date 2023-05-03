# Steps:
    #  1. Move gripper above the handle
    #  2. Push down on the handle
    # First, position the gripper above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.move("gripper above handle")
    # Once the gripper is above the handle, push down on the handle.
    if check("the robot's gripper is above the handle"):
        robot.push("down on handle")