# Steps:
    #  1. Put gripper above the hole
    #  2. Drop gripper around the peg inside the hole
    #  3. Close gripper around the peg
    #  4. Pull the peg out of the hole
    #  5. Move the peg to the goal location
    # First, put the gripper roughly above the hole so that we don't hit anything
    # while trying to grab the peg.
    if check("the robot's gripper is not above the hole"):
        robot.place("gripper above hole")
    # If the gripper isn't around the peg inside the hole yet, move it down and
    # put it around the peg.
    if check("the robot's gripper is not around peg inside hole and the robot's gripper is open"):
        robot.drop("gripper around peg inside hole")
    # If the gripper is around the peg inside the hole but not closed yet, close
    # it to grab the peg.
    if check("the robot's gripper is around peg inside hole and the robot's gripper is open"):
        robot.close("gripper around peg inside hole")
    # If the gripper is closed around the peg, we should be able to pull it out
    # of the hole.
    if check("the robot's gripper is around peg inside hole and the robot's gripper is not around hole"):
        robot.pull("peg out of hole")
    # If the gripper is holding onto the peg and is not near any obstacles or
    # the hole, move it to the goal location.
    if check("the robot's gripper is around peg and not near hole or obstacles"):
        robot.place("peg at goal")