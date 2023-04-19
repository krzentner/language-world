
    # Steps:
    #  1. Put gripper above wrench
    #  2. Drop gripper down around wrench
    #  3. Line up wrench with peg
    #  4. Put wrench around peg
    # First, move the gripper above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.put("gripper above wrench")
    # Then, put the gripper around the wrench.
    if check("the robot's gripper is not around wrench and the robot's gripper is open"):
        robot.drop("gripper around wrench")
    # Now, move the gripper with the wrench to the left or right to line up the
    # wrench with the peg.
    if check("the wrench is not horizontally lined up with the peg and the robot's gripper is around the wrench"):
        robot.align("gripper to peg")
    # Finally, move the robot's gripper toward the peg so that the wrench goes
    # around the peg.
    if check("the robot's gripper is forward aligned with the peg and the robot's gripper is around the wrench"):
        robot.push("wrench around peg")