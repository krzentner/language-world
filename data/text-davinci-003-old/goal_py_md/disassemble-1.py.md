
    # Steps:
    #  1. Put the gripper above the wrench
    #  2. Trap the wrench by closing the gripper
    #  3. Move the wrench up to release it from the peg
    # First, put the gripper roughly above the wrench, so that we don't bump it while
    # trying to grab it. 
    if check("the robot's gripper is not above the wrench"):
        robot.move_gripper("above the wrench")
    # If the wrench isn't below the gripper, put it below the gripper by closing
    # the gripper.
    if check("the robot's gripper is above the wrench and the robot's gripper is open"):
        robot.move_gripper("above the wrench", close_gripper=True)
    # If the wrench is below the gripper, move the wrench up to release it from
    # the peg.
    if check("the robot's gripper is above the wrench and the robot's gripper is closed"):
        robot.move_gripper("up above the peg")