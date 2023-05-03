# Steps:
    #  1. Put the gripper above the handle
    #  2. Turn the gripper sideways and grab the handle
    #  3. Push down on the handle from the side
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.move_gripper("vertically aligned with handle")
    # If the gripper is not around the handle, turn it sideways and grab the handle.
    if check("the robot's gripper is not around handle and the robot's gripper is above handle"):
        robot.move_gripper("around the handle")
    # Once the gripper is around the handle, turn it 90 degrees and push down on the handle from the side.
    if check("the robot's gripper is around handle"):
        robot.move_gripper("sideways aligned with handle")