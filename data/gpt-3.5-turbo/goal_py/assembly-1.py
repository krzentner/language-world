# Steps:
    #  1. Put gripper above wrench
    #  2. Grab the wrench with the gripper
    #  3. Put wrench around the peg
    #  4. Use the wrench to tighten the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.move_gripper("above the wrench")
    # If the wrench is near the gripper, grab it.
    if check("the robot's gripper is near the wrench and the robot's gripper is open"):
        robot.move_gripper("around the wrench", close_gripper=True)
    # Once the gripper is wrapped around the wrench, move it towards the peg.
    # The gripper should already be lined up with the peg from the front if we
    # grabbed the wrench while it was around the peg.
    if check("the robot's gripper is around the wrench and the wrench is around the peg"):
        robot.move_gripper("around the peg")
    # Use the gripper to turn the wrench to tighten the peg.
    if check("the robot's gripper is around the peg"):
        robot.move_gripper("around the peg", turn=True)