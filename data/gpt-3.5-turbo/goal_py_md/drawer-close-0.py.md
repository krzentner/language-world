# drawer-close: push the drawer close
# def drawer_close(robot):
    # Steps:
    #  1. Put gripper roughly around the drawer handle
    #  2. Push the drawer closed
    # If the gripper is not near the drawer handle, move it to the drawer handle.
    # We don't need to be careful about the direction, since the drawer is large
    # and we're just pushing it (unlike when opening the drawer).
    if check('the robot\'s gripper is not near the drawer handle'):
        robot.move_gripper('near the drawer handle')
    # If the drawer is aligned with the gripper as seen from in front, we can
    # push the drawer closed.
    if check('the robot\'s gripper is behind the drawer handle and the drawer is not fully closed'):
        robot.move_gripper('slightly above the drawer handle')
    if check('the robot\'s gripper is almost horizontally aligned with the drawer handle and the drawer is not fully closed'):
        robot.move_gripper('almost vertically aligned with the drawer handle')
    if check('the robot\'s gripper is vertically aligned with the drawer handle and the drawer is not fully closed'):
        robot.move_gripper('around the drawer handle')
    #Once the gripper is around the drawer handle, we can just push the drawer
    # closed.
    if check('the robot\'s gripper is horizontally aligned with the drawer handle and the drawer is not fully closed'):
        robot.move_gripper('behind the drawer handle')