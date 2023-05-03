
    # Steps:
    #  1. Put gripper just left of peg
    #  2. Pull the peg out
    # We need to put the robot's gripper just left of the peg, so that the robot
    # can grab the peg and pull out the peg.
    if check("the robot's gripper is not left of peg"):
        robot.put("gripper left of peg")
    # Check if the robot is near the peg, if yes pull it out.
    if check("the robot's gripper is near peg"):
        robot.pull("peg out")