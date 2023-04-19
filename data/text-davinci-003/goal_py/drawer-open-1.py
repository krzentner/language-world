
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull open the drawer
    # We need to put the gripper above the drawer handle before we can grab it.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not above the drawer handle"):
        robot.move_gripper("above the drawer handle")
    # As long as the gripper is above the drawer handle, close it and it should
    # line up.
    if check("the robot's gripper is above the drawer handle and the robot's gripper is open"):
        robot.move_gripper("around the drawer handle", close_gripper=True)
    # If the gripper is around the drawer handle, pull the drawer open.
    if check("the robot's gripper is around drawer handle"):
        robot.move_gripper("horizontally aligned with the drawer handle")