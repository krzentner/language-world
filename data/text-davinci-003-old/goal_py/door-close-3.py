
    # Steps:
    #  1. Put gripper left of the door handle
    #  2. Push the door closed
    # We don't need to be careful about the direction, since the door is large
    # and we're just pushing it (unlike when opening the door).
    # If the door handle is right of the robot's gripper, we should move the
    # gripper near the door handle to start pushing.
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("near the door handle")
    # If the robot's gripper is near the door handle, we can push the door
    # closed.
    if check("the door handle is right of the robot's gripper"):
        robot.move_gripper("above the door handle")