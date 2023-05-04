
    # Steps:
    #  1. Put gripper above peg
    #  2. Drop gripper down onto peg
    #  3. Close gripper around peg
    #  4. Pull peg from wrench
    # First, put the gripper roughly above the peg.
    if check("the robot's gripper is not above peg and the robot's gripper is not vertically aligned with peg"):
        robot.put("gripper above peg")
    # If the gripper isn't around the peg, put it around the peg.
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.drop("gripper around peg")
    # If the gripper is near the peg and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    # The peg is above the wrench, so move the peg up and hopefully it will
    # come off the wrench.
    if check("the peg is above the wrench"):
        robot.lift("the peg above the wrench")

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
        robot.grab("drawer handle")
    # If the drawer is aligned with the gripper as seen from in front, we can
    # push the drawer closed.
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.push("drawer closed")

# window-close: slide the window closed to the right
def window_close(robot):
    # Steps:
    #  1. Put gripper left of the window handle
    #  2. Start pushing against the window handle to close the window
    #  