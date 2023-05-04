
    # Steps:
    #  1. Push against the front left corner of the plate
    #  2. Slide the plate to the goal
    # To slide the plate to the side, push it from one corner
    # If the plate is not in front of the gripper, we should move the gripper to
    # the plate.
    if check("the plate is not in front of the gripper"):
        robot.push("the gripper into the front left corner of the plate")
    # If the plate is starting to be in front of the gripper, we can probably
    # start sliding the plate towards the goal.
    if check("the plate is in front of the gripper"):
        robot.slide("the plate to the goal")

# drawer-close: push the drawer closed
def drawer_close(robot):
    # Steps:
    #  1. Put gripper near drawer handle
    #  2. Push drawer closed
    # If the gripper is not around the drawer handle, move the gripper close
    # enough to start pushing the drawer.
    if check("the robot's gripper is not around drawer handle"):
        robot.grab("drawer handle")
    # If the gripper is in front of the drawer handle, start pushing the drawer
    # closed.
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.push("drawer closed")

# drawer-open: pull the drawer open
def drawer_open(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull drawer open
    # First, put the gripper mostly above the drawer handle.
    if check("the robot's gripper is not almost vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with the drawer handle and the robot's gripper is open"):
        robot.put("gripper around drawer handle")
    # As long as the gripper is still vertically aligned with the drawer handle,
    # it's being opened, so keep pulling.
    if