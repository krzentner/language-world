# peg-unplug-side: pull the peg out from the side
# def peg_unplug_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Align the peg in the unplugging position
    #  4. Pull the peg out from the hole
    # Put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the peg is not in the correct position for unplugging, align it.
    if check("the peg is not in unplugging position"):

        robot.move_gripper("in unplugging position")
    # Pull the peg out from the hole.
    if check("the peg is in unplugging position and the robot's gripper is holding onto the peg"):
        robot.move_gripper("above the peg and left of the hole")