
    # Steps:
    #  1. Put gripper right of the handle
    #  2. Move the gripper to the left and grip the handle
    #  3. Turn handle to the right
    # To start, put the gripper right of the handle.
    if check("the handle is right of the robot's gripper and the robot's gripper is not near handle"):
        robot.move("gripper to right of handle")
    # If the gripper is near the handle, start turning it to the right.
    if check("the robot's gripper is near handle"):
        robot.turn("handle right")
    # If the handle is starting to become left of the gripper, turn it faster to
    # make it easier to close.
    if check("the handle is left of the robot's gripper"):
        robot.turn("handle right faster")