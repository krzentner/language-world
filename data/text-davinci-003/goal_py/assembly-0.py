
    # Steps:
    #  1. Get gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Line the wrench up with the peg
    #  4. Wrap the wrench around the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.move_gripper("above the wrench", close_gripper=True)
    # If the wrench is not forward of the gripper, move the gripper forward to
    # grab the wrench.
    if check("the robot's gripper is forward aligned with the peg"):
        robot.move_gripper("right of the wrench", close_gripper=True)
    # Once the gripper has the wrench, move it to the side and start wrapping the
    # wrench around the peg.
    if check("the robot's gripper is horizontally aligned with peg"):
        robot.move_gripper("above the wrench")
    # Once the wrench is in place, wrap it around the peg.
    if check("the robot's gripper is forward aligned with peg and the robot's gripper is not horizontally aligned with the peg"):
        robot.move_gripper("right of the wrench")