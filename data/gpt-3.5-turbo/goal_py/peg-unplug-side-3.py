# Steps:
    #  1. Put gripper around peg, holding onto it lightly
    #  2. Slide the peg out of the hole
    # If the peg is not in the gripper, move the gripper near it and grab onto
    # it lightly.
    if check("the peg is not in the robot's gripper"):
        robot.move_gripper("around the peg", close_gripper=False)
    # Once we have a light grip on the peg, slide it out of the hole by sliding
    # the gripper.
    if check("the robot's gripper is around the peg"):
        robot.move_gripper("near the hole")