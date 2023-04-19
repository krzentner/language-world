# Steps:
    #  1. Put gripper left of the handle
    #  2. Start pulling the handle up
    #  3. Pull the handle up harder
    # If the handle is right of the robot's gripper, we should move the
    # gripper near the handle to start pulling.
    if check("the robot's gripper is not near the handle"):
        robot.move_gripper("near the handle")
    # If the robot's gripper is near the handle we can probably start pulling it
    # up now by moving the gripper right.
    if check("the handle is left of the robot's gripper and the robot's gripper is not aligned with the handle"):
        robot.move_gripper("aligned with the handle")
    # If the robot's gripper is aligned with the handle, we can pull harder now
    if check("the robot's gripper is aligned with the handle"):
        robot.move_gripper("above the handle")