
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Pull handle up
    # We don't have to be particularly precise, since the handle is large, so we
    # just have to get the gripper above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.move("gripper above handle")
    # Once the gripper is above the handle, align it.
    if check("the robot's gripper is above handle and the robot's gripper is open"):
        robot.drop("gripper around handle")
    # As long as the gripper is around the handle, pull it.
    if check("the robot's gripper is around handle"):
        robot.pull("handle up")