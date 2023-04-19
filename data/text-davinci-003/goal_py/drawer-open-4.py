
    # Steps:
    #  1. Put gripper left of the drawer handle
    #  2. Pull on the drawer handle to open the drawer
    #  3. Push open the drawer
    # If the the drawer handle is right of the robot's gripper, we should move the
    # gripper near the drawer handle to start pulling
    if check("the robot's gripper is right of the drawer handle"):
        robot.move_gripper("near the drawer handle", close_gripper=True)
    # Once the gripper is near the drawer handle and closed, the robot can pull
    # on the drawer handle.
    if check("the robot's gripper is around drawer handle"):
        robot.move_gripper("left of the drawer handle")
    # Once the drawer handle is aligned with the gripper from the front, we can
    # push the drawer open.
    if check("the robot's gripper is forward aligned with the drawer handle"):
        robot.move_gripper("around the drawer handle")