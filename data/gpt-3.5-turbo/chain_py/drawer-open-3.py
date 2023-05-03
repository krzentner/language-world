# Steps:
    #  1. Put gripper near right edge of drawer handle
    #  2. Pull the drawer open
    # If the gripper is not near the right edge of the drawer handle, move it
    # there.
    # We don't need to be careful about the direction, since the drawer is large
    # and we're just pulling it (unlike when closing the drawer).
    if check("the robot's gripper is not near the right edge of the drawer handle"):
        robot.move("gripper to right edge of drawer handle")
    # If the gripper is near the right edge of the drawer handle, it should
    # be able to grab it.
    if check("the robot's gripper is near the right edge of the drawer handle and the robot's gripper is open"):
        robot.drop("gripper around drawer handle")
    # If the gripper has grabbed the handle, start pulling to open the drawer.
    # We should keep pulling while the gripper is still near the handle.
    # We don't need to be careful about the direction, since the drawer is large
    # and we're just pulling it (unlike when closing the drawer).
    if check("the robot's gripper is near the drawer handle"):
        robot.pull("drawer open")