# peg-unplug-side: grab the peg and pull it out from the side
def peg_unplug_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line up the gripper to pull the peg out
    #  4. Pull the gripper sideways to unplug the peg

    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")

    # If the peg becomes left of the gripper, go back to putting the gripper above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it from the front
    # instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")

    # As long as the gripper is still mostly around the peg and the peg isn't lined
    # up with the gripper for unplugging, line up the gripper to pull the peg out.
    if check("the robot's gripper is forward aligned with the peg and the peg is not aligned with the gripper for unplugging"):
        robot.align("gripper for unplugging")

    # If the gripper is aligned to unplug the peg, pull the gripper sideways to unplug the peg.
    if check("peg is now aligned with the gripper for unplugging"):
        robot.pull("gripper sideways to unplug peg")