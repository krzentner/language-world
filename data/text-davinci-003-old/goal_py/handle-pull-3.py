
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Pull the handle up
    # We need to put the gripper above the handle before we can grab it, because
    # of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.move_gripper("vertically aligned with the handle")
    # Once the gripper is lined up above the handle, we should be able to grab
    # the handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not around handle"):
        robot.move_gripper("around the handle", close_gripper=True)
    # Once the gripper is around the handle, we can just pull it up.
    if check("the robot's gripper is around handle"):
        robot.move_gripper("near the handle")