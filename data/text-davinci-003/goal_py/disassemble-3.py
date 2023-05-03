
    # Steps:
    #  1. Put gripper above wrench
    #  2. Grab wrench with gripper
    #  3. Pull wrench off peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with wrench"):
        robot.move_gripper("vertically aligned with the wrench")
    # If the wrench isn't below the gripper, go back to putting the gripper
    # above the wrench.
    if check("wrench is not left of the robot's gripper and wrench is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the wrench", close_gripper=True)
    # Once the wrench is in front of the robot's gripper, pull it off the peg.
    if check("the robot's gripper is vertically aligned with wrench"):
        robot.move_gripper("above the peg")