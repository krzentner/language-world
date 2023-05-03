
    # Steps:
    #  1. Put gripper left of the door handle
    #  2. Push the door closed
    # Since we need the gripper to stay around the door handle to hold it in
    # place, we need to be careful about where we put the gripper.
    # If the gripper is not left of the door handle, move it left of the door
    # handle to start pushing.
    if check("the robot's gripper is not left of door handle"):
        robot.move_gripper("left of the door handle", close_gripper=True)
    # If the robot's gripper is left of door handle, we can start pushing it by
    # moving the gripper right.
    if check("the robot's gripper is left of the door handle"):
        robot.move_gripper("vertically aligned with the door handle")