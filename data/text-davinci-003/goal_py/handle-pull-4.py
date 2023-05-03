
    # Steps:
    #  1. Put gripper above the handle
    #  2. Drop gripper around the handle
    #  3. Pull up the handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.move_gripper("vertically aligned with the handle", close_gripper=True)
    # If the gripper is almost lined up (but not quite), closing it should line it
    # up all the way.
    if check("the robot's gripper is almost vertically aligned with the handle"):
        robot.move_gripper("above the handle")
    # If the gripper is lined up, pull up the handle.
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.move_gripper("up the handle")