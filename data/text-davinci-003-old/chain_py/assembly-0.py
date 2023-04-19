
    # Steps:
    #  1. Put gripper above the peg
    #  2. Drop gripper around peg
    #  3. Put wrench around peg
    # First, move the robot's gripper above the peg so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the peg"):
        robot.put("gripper above peg")
    # If the gripper isn't around the peg, put it around the peg.
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.drop("gripper around peg")
    # If the gripper is near the peg and open, we can put the wrench around the
    # peg by closing the gripper.
    if check("the robot's gripper is near peg and the robot's gripper is open"):
        robot.close("wrench around peg")