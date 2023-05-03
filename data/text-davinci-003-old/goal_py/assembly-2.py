
    # Steps:
    #  1. Put gripper above peg
    #  2. Grab some part of the wrench
    #  3. Put the wrench around the peg
    #  4. Put the wrench on the peg
    # Firstly, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the gripper is over the peg, but not grabbing a part of the wrench, grab
    # a part of the wrench.
    if check("the robot's gripper is vertically aligned with the peg and the robot's gripper is not around the wrench"):
        robot.move_gripper("near the wrench")
    # If the gripper is around the wrench and the peg is not paired up with the
    # wrench, start doing so.
    if check("the robot's gripper is around the wrench and the peg is not paired with the wrench"):
        robot.move_gripper("around the peg")
    # Once the peg and the wrench are paired up, move the wrench onto the peg.
    if check("the robot's gripper is around the wrench and the peg is paired with the wrench"):
        robot.move_gripper("above the peg")