
    # Steps:
    #  1. Put gripper left of the window handle
    #  2. Push the window closed
    # If the gripper isn't aligned with the window handle, move it to the window
    # handle.
    if check("the robot's gripper is forward aligned with the window handle"):
        robot.move_gripper("vertically aligned with the window handle")
    # Once the gripper is aligned with the window handle, push the window closed
    # by pushing the gripper right.
    if check("the robot's gripper is left of the window handle"):
        robot.move_gripper("near the window handle", close_gripper=True)

# peg-unstack-side: grab the peg and lift it off the other peg, setting it to
# the side
def peg_unstack_side(robot):
    # Steps:
    #  1. Put gripper above the upper peg
    #  2. Grab the upper peg with the gripper
    #  3. Lift the upper peg off the lower peg
    # First, put the gripper above the upper peg.
    if check("the robot's gripper is not vertically aligned with the upper peg"):
        robot.move_gripper("vertically aligned with the upper peg")
    # If the peg is left of the gripper, go back to putting the gripper above
    # the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("the upper peg is not left of the robot's gripper and the upper peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("above the upper peg")
    # As long as the upper peg is mostly above the lower peg and the gripper is
    # mostly around the upper peg, we can lift it off the other peg.
    if check("the upper peg is above the lower peg"):
        robot.move_gripper("vertically aligned with the upper peg", close_gripper=True)

# drawer-close: push the drawer close
def drawer_close(robot):
    # Steps:
    #  1. Put gripper roughly around the drawer handle
    #  2. Push the drawer closed
    # If the gripper is not