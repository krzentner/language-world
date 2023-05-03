
    # Steps:
    #  1. Put gripper above the handle
    #  2. Drop gripper around the handle
    #  3. Push down the handle
    #  As with drawer-open, we need to move the gripper around the our target
    # from the top.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    # When the gripper is roughly above the handle, we should be able to grab it
    # by just moving the gripper down.
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is open"):
       robot.put("gripper around handle")
    # Once the gripper is closed around the handle, we can press down on the
    # handle by just pushing on it.
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is closed"):
        robot.push("down on handle")