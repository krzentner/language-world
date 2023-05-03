# Steps:
    #  1. Put gripper roughly around the drawer handle
    #  2. Pull the drawer open
    # If the gripper isn't near the drawer handle, move it there roughly.
    if check("the robot's gripper is not near the drawer handle"):
        robot.move_gripper("near the drawer handle")
    # If the drawer isn't already open, pull it open.
    # Before pulling the drawer, we need to ensure that the gripper is to the
    # left and that the gripper is facing sort of downwards as seen from the
    # front, so that we aren't accidentally pressing on the drawer instead of
    # pulling it.
    if check("the robot's gripper is almost vertically aligned with the drawer handle " +
             "and the robot's gripper is not left of the drawer handle"):
        robot.move_gripper("left of the drawer handle")
    # Once the gripper is in position, pulling the drawer should be a matter of
    # pulling it towards the robot.
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.move_gripper("right of the drawer handle")