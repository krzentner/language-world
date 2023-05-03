# Steps:
    #  1. Put gripper to the right of the handle (or left if the handle opens to
    #     the left)
    #  2. Push down on the handle from the side
    # Determine which direction the handle opens in based on the current
    # position of the gripper and the handle.
    if check("the handle is right of the robot's gripper"):
        open_direction = "left"
    elif check("the handle is left of the robot's gripper"):
        open_direction = "right"
    # Move the gripper to the appropriate side of the handle.
    if open_direction == "left":
        if check("the robot's gripper is not to the left of the handle"):
            robot.move("gripper to left of handle")
    else:
        if check("the robot's gripper is not to the right of the handle"):
            robot.move("gripper to right of handle")
    # Now that the gripper is on the appropriate side of the handle, push down
    # on the handle from the side.
    if check("the gripper is at the side of the handle"):
        robot.push("down on handle from the side")