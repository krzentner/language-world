# peg-unplug-side: grab the peg and pull the it out from the side
def peg_unplug_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Pull the peg out of the hole from the side
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the peg is not in front of the gripper, move the gripper to the side of the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("right of the peg", close_gripper=True)
    # Once the gripper is around the middle of the peg, move the gripper down to grip the peg tightly.
    if check("the robot's gripper is near the center of the peg"):
        robot.move_gripper("above the peg", close_gripper=True)
    # Now move the gripper to line up the peg with the hole.
    if check("peg is not horizontally aligned with hole"):
        robot.move_gripper("horizontally aligned with hole")
    # Finally, with the peg aligned with the hole, pull it out from the side.
    if check("the robot's gripper is forward aligned with the peg and the peg is aligned with the hole"):
        robot.move_gripper("left of the peg")