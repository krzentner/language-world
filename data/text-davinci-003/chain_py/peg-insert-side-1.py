
    # Steps:
    #  1. Pick up peg
    #  2. Insert peg in side of hole
    # First, grab the peg by lining up the gripper roughly above the peg and
    # closing the gripper around it.
    if check("the robot's gripper is not above the peg and the robot's gripper is open"):
        robot.put("gripper above peg")
    if check("the robot's gripper is above the peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    # Now that the peg is in the gripper, we need to line up the peg with the
    # hole from the side before inserting it.
    if check("the robot's gripper is above the peg and the robot's gripper is closed"):
        robot.move("peg side of hole")
    # Finally, insert the peg.
    if check("the peg is aligned side of hole"):
        robot.insert("peg in side of hole")