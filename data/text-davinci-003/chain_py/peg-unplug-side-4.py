
    # Steps:
    #  1. Put gripper left of peg
    #  2. Grab peg with gripper
    #  3. Pull peg out from hole
    # First, move the robot's gripper to the left of the peg.
    if check("the robot's gripper is not aligned with the peg and the peg is right of the robot's gripper"):
        robot.move("gripper to left of peg")
    # Once the gripper is aligned with the peg, we can grab the peg by closing the
    # gripper.
    if check("the robot's gripper is aligned with the peg and the robot's gripper is open and the peg is left of the robot's gripper"):
        robot.close("gripper around peg")
    # We closed the gripper and we should now have grabbed the peg, so pull the
    # peg to remove it from the hole.
    if check("the robot's gripper is aligned with the peg and the robot's gripper is closed"):
        robot.pull("peg out from the hole")