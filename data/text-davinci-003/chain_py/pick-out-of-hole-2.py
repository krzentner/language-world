
    # Steps:
    #  1. Put gripper above peg
    #  2. Drop gripper around peg
    #  3. Close gripper around peg
    #  4. Pull peg out of the hole
    #  5. Move peg to goal
    # Put the gripper above the peg so we can grab it easily.
    if check("the robot's gripper is not above the peg"):
        robot.put("gripper above peg")
    # If the peg is above and left of the gripper, move the gripper to the peg
    # to grab it by closing the gripper.
    if check("the robot's gripper is not near the peg and the robot's gripper is vertically aligned with the peg"):
        robot.drop("gripper around peg")
    # If the gripper is near the peg and open, try to grab it by closing the
    # gripper around it.
    if check("the robot's gripper is near the peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    # Once the peg is held by the robot, try to pull it out of the hole.
    if check("the robot's gripper is closed and not pulling the peg up"):
        robot.pull("up on peg")
    # Once the peg is out of the hole and in the gripper, move it to the goal.
    if check("the peg is not near the hole"):
        robot.place("peg at goal")