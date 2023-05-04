
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window open harder
    # If the the window handle is left of the robot's gripper, we should move the
    # gripper near the window handle to start pushing
    if check("the window handle is left of the robot's gripper"):
        robot.move_gripper("left of the window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window open now by moving the gripper left.
    if check("the window handle is left of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move_gripper("almost vertically aligned with the window handle")
    # If the robot's gripper is starting to be in front of the window handle,
    # push harder.
    if check("the robot's gripper is near the window handle"):
        robot.move_gripper("forward aligned with the window handle")

# drawer-close-side: push the drawer close from the side
def drawer_close_side(robot):
    # Steps:
    #  1. Put gripper below drawer handle
    #  2. Push the drawer closed from the side
    # We need to put the gripper above the drawer handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not almost vertically aligned with drawer handle"):
        robot.move_gripper("almost vertically aligned with the drawer handle")
    # Once the gripper is lined up above the drawer handle, we can just push the
    # drawer closed.
    if check("the robot's gripper is almost vertically aligned with drawer handle"):
        robot.move_gripper("below the drawer handle")

# drawer-open-side: pull the drawer open from the side
def drawer_open_side(robot):
    # Steps:
    #  1. Put gripper below drawer handle
    #  2. Drop gripper onto drawer handle
    #  3. Pull the drawer open from the side
    # First, put the gripper mostly above the drawer handle.
    if check("the robot