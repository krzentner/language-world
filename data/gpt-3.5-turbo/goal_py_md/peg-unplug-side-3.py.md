# peg-unplug-side: grab the peg and pull it out from the side
def peg_unplug_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Pull the peg out from the side
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    # As long the gripper is still mostly around the peg, try to pull it out to
    # the side.
    if check("the robot's gripper is around the peg"):
        robot.move_gripper("left of the peg")
    # If the gripper is left of the peg and is still around the peg, pull the peg
    # out of the hole.
    if check("the robot's gripper is left of the peg"):
        robot.move_gripper("away from the hole")