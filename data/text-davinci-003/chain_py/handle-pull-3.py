
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Pull up the handle
    # We have to put the gripper above the handle first, in order to line it up
    # properly.
    if check("the robot's gripper is not almost vertically aligned with handle"):
        robot.put("gripper above handle")
    # As long as the gripper is almost lined up, closing it around the handle
    # should line it up all the way.
    if check("the robot's gripper is almost vertically aligned with the handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    # As long as the gripper is still vertically aligned with the handle, pull
    # it upward.
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.pull("upward on handle")