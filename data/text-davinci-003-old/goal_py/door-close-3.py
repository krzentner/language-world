
    # Steps:
    #  1. Put gripper left of the door handle
    #  2. Start pushing against the door handle to close the door
    #  3. Push the door closed harder
    # First, put the gripper left of the door handle.
    if check("the robot's gripper is in front of the door handle"):
        robot.move_gripper("left of the door handle")
    # If the door handle is right of the gripper, maybe the gripper can push the
    # door closed.
    if check("the door handle is right of the robot's gripper and the robot's gripper is not near the door handle"):
        robot.move_gripper("almost vertically aligned with the door handle")
    # If the grippers is starting to be in front of the door handle, push harder.
    if check("the robot's gripper is near the door handle"):
        robot.move_gripper("forward aligned with the door handle")