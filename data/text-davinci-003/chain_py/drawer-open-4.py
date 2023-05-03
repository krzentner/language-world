
    # Steps:
    #  1. Put gripper forwards of the drawer handle
    #  2. Drop gripper around the drawer handle
    #  3. Pull open the drawer
    # First, put the gripper to the front of the drawer handle.
    # This is the opposite of when we are closing the drawer.
    if check("the robot's gripper is not front of the drawer handle and the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    # As long as the gripper is still in front of the drawer handle, likely still
    # grabbing it, we can pull the drawer open.
    if check("the robot's gripper is forward aligned with draw handle"):
        robot.pull("drawer open")