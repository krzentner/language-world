# Steps:
    #  1. Put gripper left of the drawer handle
    #  2. Pull the drawer open
    # If the gripper is not left of the drawer handle, move it to the left of the
    # drawer handle.
    # Because the drawer is large, we don't need to be too careful about the
    # lateral position of the gripper, just that it's on the left side of the
    # handle.
    if check("the robot's gripper is not left of the drawer handle"):
        robot.move("gripper to left of drawer handle")
    # As long as the gripper is still left of the handle, it's being opened, so
    # keep pulling.
    if check("the robot's gripper is left of the drawer handle"):
        robot.pull("drawer open")