# Steps:
    #  1. Put gripper above wrench
    #  2. Close the gripper around the wrench
    #  3. Put the gripper with the wrench around the peg
    #  4. Turn the wrench to tighten it around the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.put("gripper above wrench")
    # If the gripper is above the wrench, close the gripper around it.
    if check("the robot's gripper is above the wrench and the robot's gripper is open"):
        robot.grab("wrench")
    # If the wrench is grabbed by the gripper, put it around the peg.
    # Because the wrench is a long object, check if the wrench is lined up with
    # the peg from the front instead of around it.
    if check("the wrench is grabbed and the wrench is not forward aligned with the peg"):
        robot.move("gripper with wrench to peg")
    # If the gripper with the wrench is around the peg, turn the wrench to
    # tighten it.
    if check("the gripper with the wrench is around the peg"):
        robot.rotate("wrench to tighten")