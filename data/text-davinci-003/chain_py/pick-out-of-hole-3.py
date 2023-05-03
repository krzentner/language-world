
    # Steps:
    #  1. Put gripper sides of peg
    #  2. Close gripper around peg
    #  3. Lift the peg out of the hole
    #  4. Place the peg at the goal
    # First, put the gripper to the sides of the peg, so it can grab the peg
    # properly.
    if check("the robot's gripper is not to the sides of the peg"):
        robot.put("gripper to sides of peg")
    # When the gripper is ready, try to close it around the peg.
    if check("the robot's gripper is to the sides of the peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    # If the robot's gripper is now closed and it's still near the peg, try to
    # lift the peg out of the hole.
    # Just lift the gripper up.
    if check("the robot's gripper is around the peg and the robot's gripper is closed"):
        robot.lift("gripper")
    # If the peg is now off the ground, move it to the goal.
    if check("the peg is off the ground"):
        robot.place("peg at goal")