
    # Steps:
    #  1. Put gripper around the drawer handle
    #  2. Pull on the drawer handle
    # To open the drawer, we need to be able to get at the handle from the side,
    # so move the gripper to the side of the handle.
    if check("the robot's gripper is not left of drawer handle"):
        robot.put("gripper left of drawer handle")
    # Now that everything is lined up, the robot can pull open the drawer.
    if check("the robot's gripper is left of drawer handle"):
        robot.pull("drawer open")