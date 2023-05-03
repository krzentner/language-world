
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Pull handle up
    # First, put the gripper above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.put("gripper above handle")
    # Now that the gripper is above the handle, we can grab it by dropping it
    # down around it.
    if check("the robot's gripper is above handle and the robot's gripper is open"):
        robot.drop("gripper around handle")
    # Once the gripper is around the handle, it should be horizontal with the
    # handle, so we can just pull up the handle.
    if check("the robot's gripper is around handle"):
        robot.pull("handle up")