
    # Steps:
    #  1. Put gripper above the handle
    #  2. Drop gripper around handle
    #  3. Push the handle down
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    # If the gripper is almost lined up with the handle, closing it should line
    # it up all the way.
    if check("the robot's gripper is almost vertically aligned with handle and the robot's gripper is open"):
        robot.drop("gripper around handle")
    # Once it's lined up, just push down on the handle.
    if check("the robot's gripper is vertically aligned with handle"):
        robot.push("down on handle")