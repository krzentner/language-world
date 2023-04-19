
    # Steps:
    #  1. Put gripper above the handle
    #  2. Drop gripper around handle
    #  3. Pull up on the handle
    # We need to put the gripper above the handle before we can grab it, because
    # of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    # Once the gripper is lined up, we can grab the handle by moving the gripper
    # around it.
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is not around the handle"):
        robot.move_gripper("around the handle")
    # Once the gripper is around the handle, we can just pull the handle up.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("upward")