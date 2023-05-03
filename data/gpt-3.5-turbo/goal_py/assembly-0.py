# Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Position the wrench around the peg
    #  4. Tighten the wrench
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.move_gripper("vertically aligned with the wrench")
    # Once the gripper is above the wrench, grab it with the gripper.
    if check("the robot's gripper is above the wrench and the gripper is open"):
        robot.move_gripper("around the wrench")
    # Once the gripper is around the wrench, position the wrench around the peg.
    if check("the robot's gripper is around the wrench"):
        robot.move_gripper("around the peg")
    # Now that the wrench is wrapped around the peg, tighten it.
    if check("the robot's gripper is positioned correctly around the peg"):
        robot.move_gripper("tight around the peg")