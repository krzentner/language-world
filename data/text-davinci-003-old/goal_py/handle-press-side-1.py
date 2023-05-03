
    # Steps:
    #  1. Put gripper above the handle
    #  2. Drop gripper around handle
    #  3. Push the handle down
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.move_gripper("vertically aligned with the handle")
    # Once the gripper is lined up above the handle, we can push the handle down
    # by moving the gripper around the handle.
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is not around handle"):
        robot.move_gripper("around the handle")
    # Once the gripper is around the handle, we can just push the handle down.
    if check("the robot's gripper is around handle"):
        robot.move_gripper("left of the handle")