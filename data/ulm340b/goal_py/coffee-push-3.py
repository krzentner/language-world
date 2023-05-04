
    # Steps:
    #  1. Put gripper roughly above mug
    #  2. Grab mug with gripper
    #  3. Push mug to goal
    # First, put the gripper roughly above the mug, so that we don't bump the
    # mug while grabbing it.
    if check("the robot's gripper is not above the mug"):
        robot.move_gripper("above the mug")
    # Put the robot's gripper above the mug.
    if check("the robot's gripper is not vertically aligned with mug and the robot's gripper is not near mug"):
        robot.move_gripper("vertically aligned with the mug")
    # If the mug is below the gripper, we've probably grabbed it and can start
    # moving it.
    if check("the robot's gripper is vertically aligned with mug and the mug is below the robot's gripper"):
        robot.move_gripper("above the target location")

# drawer-close: push the drawer closed
def drawer_close(robot):
    # Steps:
    #  1. Put gripper roughly around the drawer handle
    #  2. Push the drawer closed
    # If the gripper is not near the drawer handle, move it to the drawer
    # handle.
    # We don't need to be careful about the direction, since the drawer is large
    # and we're just pushing it (unlike when opening the drawer).
    if check("the robot's gripper is not near the drawer handle"):
        robot.move_gripper("near the drawer handle")
    # If the drawer is aligned with the gripper as seen from in front, we can
    # push the drawer closed.
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.move_gripper("around the drawer handle")

# drawer-open: pull the drawer open
def drawer_open(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull open the drawer
    # We need to put the gripper above the drawer handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot