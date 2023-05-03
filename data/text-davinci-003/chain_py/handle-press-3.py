
    # Steps:
    #  1. Put gripper on the left side of the handle
    #  2. Push down on the handle
    # First, move the gripper to the left side of the handle, because the left
    # side is wide open.
    # This should line up the gripper with the handle.
    if check("the robot's gripper is not horizontally aligned with the handle"):
        robot.move("gripper to left side of the handle")
    # Now that the gripper is lined up, just push down on the handle.
    if check("the robot's gripper is horizontally aligned with the handle"):
        robot.push("down on the handle")