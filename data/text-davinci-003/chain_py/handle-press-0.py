
    # Steps:
    #  1. Line up the gripper with the handle
    #  2. Push down on the handle
    # To press the handle, we first must line the gripper up with the handle to
    # make sure that the gripper can push the handle down.
    # Line up the robot's gripper with the handle.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    # Now that the gripper is lined up, just push down on the handle.
    if check("the robot's gripper is vertically aligned with handle"):
        robot.push("down on handle")