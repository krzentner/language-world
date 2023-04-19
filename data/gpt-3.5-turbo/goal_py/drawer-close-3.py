# Steps:
    # 1. Put gripper roughly around the drawer handle
    # 2. Push the drawer closed
    # If the gripper is not near the drawer handle, move it to the drawer handle.
    if check("the robot's gripper is not near the drawer handle"):
        robot.move_gripper("near the drawer handle")
    # If the drawer is aligned with the gripper as seen from in front, we can
    # push the drawer closed.
    if check("the robot's gripper is forward aligned with the drawer handle"):
        robot.move_gripper("around the drawer handle")