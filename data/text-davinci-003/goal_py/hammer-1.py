
    # Steps:
    #  1. Put gripper above the hammer handle
    #  2. Drop gripper on handle
    #  3. Start swinging the hammer
    #  4. Hit the nail
    # First, put the gripper directly above the hammer handle.
    if check("the robot's gripper is not vertically aligned with the hammer handle"):
        robot.move_gripper("vertically aligned with the hammer handle")
    # As long as the gripper is still lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is vertically aligned with hammer handle"):
        robot.move_gripper("around the hammer handle")
    # Once the gripper is on the handle, we can start swinging.
    if check("the robot's gripper is around the hammer handle"):
        robot.move_gripper("just above the nail")
    # When the hammer is above the nail, we can start hitting it.
    if check("the hammer is just above nail"):
        robot.move_gripper("into the nail")