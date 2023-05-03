# Steps:
    #  1. Put gripper above wrench
    #  2. Grab the wrench with the gripper
    #  3. Put gripper around peg
    #  4. Twist the wrench to tighten the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not above wrench"):
        robot.put("gripper above wrench")
    # If the gripper is above the wrench, grab it.
    if check("the robot's gripper is above wrench and the robot's gripper is open"):
        robot.grab("wrench")
    # If the wrench is grabbed, try to put it around the peg.
    if check("the robot's gripper is holding wrench and the robot's gripper is not around peg"):
        robot.put("gripper around peg using wrench")
    # If the gripper is around the peg and holding the wrench, try to twist the
    # wrench to tighten the peg.
    if check("the robot's gripper is around peg using wrench"):
        robot.twist("wrench to tighten peg")