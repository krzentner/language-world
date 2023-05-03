
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Move the peg sideways
    #  4. Pull the peg out
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the gripper isn't around the peg, grab it.
    if check("the robot's gripper is vertically aligned with the peg and the robot's gripper is not around peg"):
        robot.grab("peg")
    # As long as the peg is still near the gripper, try to move the peg
    # horizontally.
    if check("the robot's gripper is around the peg and the peg is not clear of the hole"):
        robot.slide("peg sideways")
    # If the peg is clear of the hole, pull it out.
    if check("the peg is clear of the hole"):
        robot.pull("peg out")