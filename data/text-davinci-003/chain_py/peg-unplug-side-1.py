
    # Steps:
    #  1. Put gripper left of the peg
    #  2. Grab the peg with the gripper
    #  3. Pull the peg out
    #  4. Move the peg away from the hole
    # If the robot's gripper is not left of the peg, move it into position.
    if check("the robot's gripper is not left of the peg"):
        robot.move("gripper left of peg")
    # When the gripper is left of the peg, close the gripper around the peg to
    # grab it so we can pull it out.
    if check("the robot's gripper is left of the peg and the gripper is open"):
        robot.close("gripper around peg")
    # If the gripper is closed and the peg is still in the hole, try to pull the
    # peg out of the hole.
    if check("the robot's gripper is left of the peg and the peg is in the hole"):
        robot.pull("peg out")
    # After pulling the peg partway out of the hole, we can move it away.
    if check("the robot's gripper is left of the peg and the peg is partly out of the hole"):
        robot.move("peg away from hole")