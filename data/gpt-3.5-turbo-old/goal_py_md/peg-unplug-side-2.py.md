# peg-unplug-side: pull the peg out from the side
# def peg_unplug_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up to the direction to remove the peg
    #  4. Pull the peg out from the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the peg is not near the gripper, move the gripper near to the peg
    # and grab the peg
    if check("the robot's gripper is not around the peg" or "the robot's gripper is open"):
        robot.move_gripper("near the peg", close_gripper=True)
    # If the peg is held by the gripper, start moving towards to the direction
    # to remove the peg.
    if check("the robot's gripper is around the peg"):
        robot.move_gripper("roughly aligned with the direction to remove the peg")
    # Once the gripper is aligned with the direction to remove the peg, pull the
    # peg outwards.
    if check("the robot's gripper is aligned with the direction to remove the peg"):
        robot.move_gripper("out of the hole")