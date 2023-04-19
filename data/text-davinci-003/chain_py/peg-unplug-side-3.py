
    # Steps:
    #  1. Put gripper above peg
    #  2. Grab peg
    #  3. Pull peg out
    # Put the gripper roughly above the peg
    if check("the robot's gripper is not roughly above peg"):
        robot.put("gripper above peg")
    # Now that the robot's gripper is above the peg, grab it and hold it firmly.
    if check("the robot's gripper is roughly above peg and the robot's gripper is open"):
            robot.grab("peg")
    # Pull the peg out.
    if check("the robot's gripper is above peg and the robot's gripper is closed"):
        robot.pull("peg out")