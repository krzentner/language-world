
    # Steps:
    #  1. Put gripper above peg
    #  2. Grab peg with gripper
    #  3. Line peg up with the hole from the side
    #  4. Pull the peg out
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the peg is right of the gripper as seen from in front, go back to
    # putting the gripper above the peg.
    # We need to check that the gripper isn't already around the peg, since the
    # peg is tall and the gripper might not be able to lift it from the side.
    if check("the peg is not above the robot's gripper"):
        robot.move_gripper("forward aligned with the peg")
    # If the gripper is around the peg and the peg is lined up with the hole to
    # the side, pull it out.
    if check("the robot's gripper is horizontay aligned with the peg and the peg is horizontally aligned with hole"):
        robot.move_gripper("above the peg")
    # If the peg is lined up with the hole, get the gripper ready for
    # unplugging.
    if check("the peg is horizontally aligned with hole"):
        robot.move_gripper("left of the peg")