
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Push the handle down
    # First, put the gripper above the handle. We have to be careful to line it up
    # vertically, since we're pushing down on a specific part of the handle.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.move_gripper("vertically aligned with the handle")
    # If the gripper is roughly lined up, we should be able to grab the handle by
    # moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is not around handle"):
        robot.move_gripper("around the handle")
    # Now we can push the handle down.
    if check("the robot's gripper is around handle"):
        robot.move_gripper("horizontally aligned with the handle")