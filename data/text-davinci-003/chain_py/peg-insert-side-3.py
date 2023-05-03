
    # Steps:
    #  1. Put gripper near the side of the peg
    #  2. Squeeze gripper to grab the peg
    #  3. Move gripper towards the hole
    #  4. Push peg into the hole
    # If the robot's gripper is not near the side of the peg, move the gripper to
    # the side the peg.
    if check("the robot's gripper is not near the side of the peg"):
        robot.grab("side of peg")
    # If the robot's gripper is near the side of the peg, close the gripper to
    # grab it.
    if check("the robot's gripper is near the side of the peg and the robot's gripper is open"):
        robot.close("gripper to grab peg")
    # If the robot's gripper is already closed around the peg, then start moving
    # towards the hole.
    if check("the robot's gripper is near the side of the peg and the robot's gripper is closed"):
        robot.put("peg near hole")
    # If the peg is near the hole and the gripper is closed around it, just push
    # the peg into the hole.
    if check("the peg is near the hole and the robot's gripper is closed"):
        robot.push("peg into hole")