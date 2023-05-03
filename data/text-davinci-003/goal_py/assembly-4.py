
    # Steps:
    #  1. Place the wrench below the peg
    #  2. Wrap the wrench around the peg
    #  3. Tighten the wrench
    # Put the robot's gripper below the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # Wrap the wrench around the peg so that the peg is in the middle.
    if check("the robot's gripper is vertically aligned with the peg and the peg is not centered in the wrench"):
        robot.move_gripper("around the peg")
    # Now that the peg is centered in the wrench, we can tighten it by pushing it
    # down.
    if check("the peg is centered in the wrench and the robot's gripper is not near the peg"):
        robot.move_gripper("near the peg")