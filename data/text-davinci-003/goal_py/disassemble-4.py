
    # Steps:
    #  1. Put gripper above wrench
    #  2. Grab wrench
    #  3. Pull wrench off of peg
    # First, move the gripper above the wrench.
    if check("the robot's gripper is not above wrench"):
        robot.move_gripper("above the wrench")
    # If the robotic gripper is lined up but not near the wrench, move it to
    # grab the wrench.
    if check("the robot's gripper is not near wrench and the robot's gripper is vertically aligned with wrench"):
        robot.move_gripper("near the wrench")
    # Now that the robot has the wrench, pull it off the peg.
    if check("the robot's gripper is near wrench"):
        robot.move_gripper("above the peg")