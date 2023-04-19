
    # Steps:
    #  1. Put gripper right of the door handle
    #  2. Start pushing against the door handle to close the door
    #  3. Push the door closed harder
    # We need to be able to align the gripper with the door handle so that we
    # can push it closed.
    # If the robot's gripper is not near the door handle, we should move the
    # gripper near the door handle to start pushing.
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("near the door handle")
    # Once the gripper is near the handle, we should be able to move it left to
    # start pushing.
    if check("the robot's gripper is near the door handle and the door handle is right of the robot's gripper"):
        robot.move_gripper("left of the door handle")
    # If the gripper starts to be in front of the door handle, we can push it
    # closed.
    if check("the robot's gripper is near the door handle and the door handle is left of the robot's gripper"):
        robot.move_gripper("near the target location")