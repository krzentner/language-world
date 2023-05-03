# Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Wrap the wrench around the peg
    # First, put the gripper roughly above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.move_gripper("above the wrench")
    # If the gripper is not around the wrench, grab it by moving the gripper
    # near it and closing the gripper.
    if check("the robot's gripper is not around the wrench and the robot's gripper is near the wrench"):
        robot.move_gripper("around the wrench", close_gripper=True)
    # If the gripper is around the wrench, move it around the peg to wrap the
    # wrench around the peg.
    if check("the robot's gripper is around the wrench"):
        robot.move_gripper("around the peg")