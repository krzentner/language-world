
    # Steps:
    #  1. Put gripper near faucet handle
    #  2. Grab faucet handle with the gripper
    #  3. Turn faucet handle right
    # If the robot's gripper is not near the faucet handle as seen from in front
    # we should move it towards the faucet handle.
    # We need to be careful about the direction when approaching so we can grab
    # it well.
    if check("the robot's gripper is not near the faucet handle"):
        robot.move_gripper("vertically aligned with the faucet handle")
    # If the faucet handle is left of the robot's gripper, go back to putting
    # the gripper above the faucet handle.
    # Because the faucet handle is a long object, check if the gripper is lined
    # up with it from the front instead of around it.
    if check("faucet handle is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the faucet handle")
    # If the faucet handle is aligned with the gripper from the front, start
    # closing the faucet by moving the gripper clockwise around it.
    if check("the robot's gripper is forward aligned with faucet handle and the robot's gripper is not around faucet handle"):
        robot.move_gripper("around faucet handle")

# drawer-close-side: push the drawer closed from the side
def drawer_close_side(robot):
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

# button-press-side: push the button down from the side
def