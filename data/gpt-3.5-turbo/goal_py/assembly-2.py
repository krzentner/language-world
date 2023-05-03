# Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Put the wrench around the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.move_gripper("vertically aligned with the wrench")
    # If the wrench is not mostly around the gripper, grab it.
    if check("the robot's gripper is vertically aligned with the wrench and the wrench is not around the gripper"):
        robot.move_gripper("above the peg")
    # Once the wrench is around the peg, we can just hold it in place.
    if check("the robot's gripper is around the peg"):
        robot.move_gripper("horizontally aligned with the peg")