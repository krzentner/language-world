
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Pull the peg out to the side
    # First, we need to move the gripper above the peg.
    if check("the robot's gripper is not above the peg"):
        robot.put("gripper above the peg")
    # If the peg isn't left of the gripper, grab it.
    if check("the peg is not left of the robot's gripper"):
        robot.grab("peg")
    # As long as the peg is left of the gripper and there's no obstruction, pull
    # the peg out to the side.
    if check("the robot's gripper is left of the peg and there is no obstruction"):
        robot.pull("peg to the side")