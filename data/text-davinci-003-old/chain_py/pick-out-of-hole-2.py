
    # Steps:
    #  1. Put gripper above peg
    #  2. Grab peg with gripper
    #  3. Lift peg out of hole
    # We need to put the gripper above the peg before we can grab it, because of
    # the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with peg"):
        robot.put("gripper above peg")
    # Once the gripper is lined up above the peg, we should be able to grab the
    # peg by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with peg and the robot's gripper is not around peg"):
        robot.put("gripper around peg")
    # Once the gripper is around the peg, try to lift it out of the hole.
    # If we can't, the gripper either isn't around the peg well enough or the
    # peg isn't able to be lifted out, so go back to an earlier step.
    if check("the robot's gripper is around peg and the robot's gripper is closed"):
        robot.lift("peg out of hole")