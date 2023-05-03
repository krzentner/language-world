# Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Line up the wrench with the peg
    #  4. Wrap the wrench around the peg to tighten it
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.move_gripper("vertically aligned with the wrench")
    # If the wrench becomes left of the gripper, go back to putting the gripper
    # above the wrench.
    # Because the wrench is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("wrench is not left of the robot's gripper and wrench is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the wrench", close_gripper=True)
    # As long the gripper is still mostly around the wrench and the wrench isn't lined
    # up with the peg, line up the wrench with the peg.
    if check("wrench is not vertically aligned with peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the wrench is lined up with the peg, wrap it around the peg to tighten it.
    if check("the robot's gripper is vertically aligned with peg"):
        robot.move_gripper("around the peg")