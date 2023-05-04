
    # Steps:
    #  1. Put gripper above the plate
    #  2. Push gripper into the plate
    #  3. Slide the plate into place
    # Since the plate is thin, we can push it around by pushing against the top
    # of the plate.
    if check("the plate is not below the robot's gripper"):
        robot.move_gripper("above the plate")
    # If the plate is roughly below the robot's gripper, we can try pushing it
    # into the right place by moving the gripper down.
    # (We can check the gripper is above the plate instead of near it because
    # the plate is so big and thin that it's hard to miss.)
    if check("the robot's gripper is above the plate"):
        robot.move_gripper("near the plate")
    # If the robot's gripper is near the plate, it's probably trapped the plate
    # and can slide it to the target location.
    if check("the plate is near the robot's gripper"):
        robot.move_gripper("above the target location")

# peg-unstack: grab the top peg and lift it up and off of the other peg
def peg_unstack(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Drop gripper around peg
    #  3. Lift the peg
    # First, put the gripper above the top peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the robot's gripper is roughly aligned with the top peg, try to drop
    # the gripper around the top peg.
    if check("the peg is not around the robot's gripper"):
        robot.move_gripper("around the peg", close_gripper=True)
    # If the robot's gripper is around the top peg, it can lift the top peg up.
    if check("the peg is above the robot's gripper"):
        robot.move_gripper("above the peg")

# window-close-topdown: push the window closed from above
def window_close_topdown(robot):
    # Steps:
