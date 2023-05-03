# Steps:
    #  1. Put gripper above the handle
    #  2. Slide gripper down around the handle
    #  3. Push gripper to press the handle down
    # We need to put the gripper above the handle before we can grab it, because
    # of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    # Once the gripper is lined up above the handle, we should be able to
    # grab the handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is not around the handle"):
        robot.move_gripper("around the handle")
    # Once the gripper is around the handle, we can push down to press the handle.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("pushing down on the handle")