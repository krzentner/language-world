
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Push handle downward
    # First, put the gripper above the handle so that it will not miss the handle
    # when coming down.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    # If the gripper is almost lined up with the handle vertically, just close
    # it to make sure that it is properly aligned.
    if check("the robot's gripper is almost vertically aligned with the handle and the robot's gripper is open"):
        robot.drop("gripper around handle")
    # If the gripper is aligned with the handle, close it and press it downward.
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is closed"):
        robot.push("downward on handle")