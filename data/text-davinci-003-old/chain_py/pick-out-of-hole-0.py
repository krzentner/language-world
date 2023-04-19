
    # Steps:
    #  1. Put gripper above the peg
    #  2. Drop gripper around peg
    #  3. Pull peg up out of the hole
    #  4. Move peg to goal
    # First, put the gripper roughly above the peg, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the peg"):
        robot.place("gripper above peg")
    # If the gripper isn't around the peg, put it around the peg.
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.drop("gripper around peg")
    # If the gripper is near the peg and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    # We closed the gripper, and the peg is still near the gripper, so maybe we
    # grabbed it.
    # Try to pull the peg out of the hole.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is around peg and the robot's gripper is closed"):
        robot.pull("peg out of hole")
    # Once the peg is out of the hole, we can move it to the goal location.
    if check("the peg is out of the hole"):
        robot.place("peg at goal")