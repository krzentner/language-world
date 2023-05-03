# Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Line the wrench up around the peg
    #  4. Tighten the wrench around the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.put("gripper above wrench")
    # If the wrench becomes unaligned with the gripper, go back to putting the
    # gripper above the wrench.
    # Because the wrench is a thin object, check if the gripper is positioned
    # around it instead of in front of it.
    if check("the wrench is not around the robot's gripper"):
        robot.grab("wrench")
    # As long as the gripper is still around the wrench and not lined up with the
    # peg, line up the wrench around the peg.
    if check("the wrench is around the robot's gripper and the wrench is not aligned around the peg"):
        robot.align("wrench around peg")
    # If the wrench is aligned around the peg, tighten it.
    if check("the wrench is aligned around the peg"):
        robot.turn("wrench to tighten around peg")