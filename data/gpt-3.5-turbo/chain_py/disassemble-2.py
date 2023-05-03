# Steps:
    #  1. Put gripper above wrench
    #  2. Drop gripper around wrench
    #  3. Rotate wrench counterclockwise to loosen it
    #  4. Lift wrench up and off the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not above wrench"):
        robot.put("gripper above wrench")
    # Once the gripper is above the wrench, we should be able to grab it by
    # moving the gripper down around it.
    if check("the robot's gripper is above wrench and the robot's gripper is not around wrench"):
        robot.drop("gripper around wrench")
    # Now that the gripper is around the wrench, we can try rotating it
    # counterclockwise to loosen it.
    if check("the robot's gripper is around wrench and the wrench is not loose"):
        robot.rotate("wrench counterclockwise")
    # We should have loosened the wrench enough to lift it off the peg. Lift the
    # wrench up and off the peg.
    if check("the robot's gripper is around wrench and the wrench is loose"):
        robot.lift("wrench off peg")