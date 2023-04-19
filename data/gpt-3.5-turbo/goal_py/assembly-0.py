# Steps:
    #  1. Put gripper above wrench and roughly around peg
    #  2. Drop gripper around wrench
    #  3. Rotate wrench around peg until it clicks into place
    # First, put the gripper roughly above the wrench and around the peg.
    if check("the robot's gripper is not above the wrench"):
        robot.move_gripper("above the wrench")
    # If the gripper is not around the wrench yet, move it there and close the
    # gripper.
    if check("the robot's gripper is not around the wrench and the robot's gripper is open"):
        robot.move_gripper("around the wrench", close_gripper=True)
    # To rotate the wrench around the peg, we need to make sure it's lined up
    # with the peg to start with.
    if check("the wrench is not almost vertically aligned with the peg"):
        robot.move_gripper("almost vertically aligned with the peg")
    # Now we can rotate the wrench around the peg. This involves:
    #   1. Rotating the wrist to be horizontally aligned with the peg.
    #   2. Adjusting the position of the gripper so that the wrench is very
    #      near or touching the peg.
    #   3. Closing the gripper a little bit to press the wrench onto the peg.
    #   4. Compressing the gripper all the way to cause the wrench to click into
    #      place around the peg.
    if check("the robot's gripper is almost horizontally aligned with the peg"):
        robot.move_gripper("almost touching the peg")
    if check("the wrench is not fully compressed around the peg"):
        robot.move_gripper("fully compressed around the peg")