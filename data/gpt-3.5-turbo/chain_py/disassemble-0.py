# Steps:
    #  1. Put gripper above wrench
    #  2. Drop gripper around wrench
    #  3. Close gripper around wrench
    #  4. Lift wrench off peg
    # First, put the gripper above the wrench so we don't bump into anything when
    # grabbing it.
    if check("the robot's gripper is not above the wrench"):
        robot.place("gripper above wrench")
    # If the gripper is not around the wrench yet, we should lower it around the
    # wrench handle now.
    if check("the robot's gripper is not around wrench and the robot's gripper is open"):
        robot.drop("gripper around wrench")
    # If the gripper is around the wrench handle and the wrench is still on the
    # peg, we should close the gripper to grab it and pull it up.
    if check("the robot's gripper is around wrench and the wrench is still on the peg"):
        robot.close("gripper around wrench")
    # Now that the gripper is closed around the wrench handle, we can lift it off
    # the peg just by moving the gripper straight up.
    if check("the robot's gripper is around wrench and the wrench is not on the peg"):
        robot.move("gripper and wrench up")