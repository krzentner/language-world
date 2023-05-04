
    # Steps:
    #  1. Put gripper left of the window handle
    #  2. Start pushing against the window handle to close the window
    #  3. Push the window closed harder
    # If the robot's gripper is not in front of the window handle, we should
    # move the gripper near the window handle to start pushing
    if check("the robot's gripper is near the window handle"):
        robot.move_gripper("near the window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window closed now by moving the gripper right.
    if check("the robot's gripper is left of the window handle"):
        robot.move_gripper("left of the window handle")

# peg-unstack: pick up the top peg off the stack
def peg_unstack(robot):
    # Steps:
    #  1. Put gripper above the top peg
    #  2. Grab the peg with the gripper
    #  3. Lift the peg off the stack
    # First, put the gripper above the top peg.
    if check("the robot's gripper is not vertically aligned with peg"):
        robot.move_gripper("vertically aligned with the top peg")
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("the peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the top peg", close_gripper=True)
    # Because the peg is on top of another peg, closing the gripper around it
    # will push it slightly out of alignment, so just move the gripper up.
    if check("the robot's gripper is forward aligned with the peg"):
        robot.move_gripper("near the target location", close_gripper=True)

# hammer-tap: hit the nail with the hammer
def hammer_tap(robot):
    # Steps:
    #  1. Put gripper above hammer
    #  2. Grab the hammer with the gripper
    #  3. Move the hammer towards the nail
    # First, put the gripper above the hammer.
    if check("the robot's