# Steps:
    #  1. Put gripper around the peg
    #  2. Grip the peg firmly
    #  3. Slide the peg to unplug it from the hole
    # First, put the gripper around the peg.
    if check("the robot's gripper is not around the peg"):
        robot.put("gripper around peg")
    # If the gripper isn't fully gripped around the peg, grip it more firmly.
    if check("the robot's gripper is around the peg but not fully closed"):
        robot.close("gripper around peg")
    # If the gripper is fully closed around the peg and the peg is aligned with
    # the hole to the side, unplug the peg by sliding it out to the side.
    if check("the robot's gripper is fully closed around the peg and the peg is horizontally aligned with hole"):
        robot.slide("peg out of hole")