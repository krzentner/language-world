# peg-unplug-side: pull the peg out from the side
# def peg_unplug_side(robot):
    # Steps:
    #  1. Put the gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Pull the peg out from the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    # If the peg is grabbed by the gripper, we can start pulling it out.
    # We should be careful not to bang it against the side of the hole as we
    # pull it out.
    if check("the robot's gripper is around the peg"):
        robot.pull("peg out of the hole")