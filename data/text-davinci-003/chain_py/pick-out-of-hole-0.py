
    # Steps:
    #  1. Put gripper near the side of the hole
    #  2. Line up the gripper with the peg
    #  3. Turn the gripper sideways
    #  4. Pull the peg out of the hole
    #  5. Place the peg at the goal
    # The peg is in the hole and the gripper needs to grab it from the side.
    # First, put the gripper near the side of the hole.
    if check("the robot's gripper is not above the side of the hole"):
        robot.place("gripper near side of hole")
    # If the gripper is close to the side of the hole, try to line up the
    # gripper with the peg.
    if check("the robot's gripper is beside the side of the hole"):
        robot.align("gripper with peg")
    # Now that the gripper is lined up with the peg, turn it sideways.
    if check("the robot's gripper is forward aligned with peg"):
        robot.rotate("gripper sideways")
    # If the gripper is almost lined up with the peg, pull the peg out.
    if check("the robot's gripper is sideways facing outward of the peg's head"):
        robot.pull("peg out of hole")
    # If the peg is out of the hole, make sure we still have it by closing the
    # gripper.
    if check("the robot's gripper is beside the head of the peg and the robot's gripper is open"):
        robot.grab("peg")
    # Now that the peg is inside the gripper, we can drop it at the goal.
    if check("the robot's gripper is beside the head of the peg and the robot's gripper is closed"):
        robot.place("peg at goal")