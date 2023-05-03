
    # Steps:
    #  1. Put robot's gripper below the drawer handle
    #  2. Pull open the drawer
    #  3. Move the drawer open farther
    # First, put the robot's gripper in front of the drawer handle.
    if check("the robot's gripper is not in front of the drawer handle"):
        robot.move_gripper("right of the drawer handle")
    # If the gripper is lined up, close it around the drawer handle.
    if check("the robot's gripper is in front of the drawer handle and the robot's gripper is not around the drawer handle"):
        robot.move_gripper("forward aligned with the drawer handle", close_gripper=True)
    # Once the gripper is around the drawer handle, pull open the drawer.
    if check("the robot's gripper is around the drawer handle"):
        robot.move_gripper("right of the drawer handle")