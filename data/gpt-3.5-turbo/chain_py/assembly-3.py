# Steps:
    #  1. Put gripper near the wrench
    #  2. Grip the wrench
    #  3. Put gripper around the peg
    #  4. Turn the wrench to tighten the peg
    # First, put the gripper near the wrench.
    if check("the robot's gripper is not near the wrench"):
        robot.place("gripper near wrench")
    # If the gripper is near the wrench but not gripping it yet, grip it.
    if check("the robot's gripper is near the wrench and the robot's gripper is open"):
        robot.grab("wrench")
    # If the gripper has the wrench and is not around the peg, put the gripper
    # around the peg.
    if check("the robot's gripper has the wrench and the gripper is not around the peg"):
        robot.put("gripper around peg")
    # If the gripper is around the peg, we can then turn the wrench to tighten
    # the peg.
    if check("the robot's gripper is around the peg and the robot's gripper has the wrench"):
        robot.turn("wrench to tighten peg")