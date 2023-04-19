# Steps:
    #  1. Put gripper around the dial
    #  2. Turn the dial to the desired position
    # First, put the gripper around the dial.
    if check("the robot's gripper is not around the dial"):
        robot.move_gripper("around the dial")
    # If the dial isn't turned to the desired position, turn it.
    if check("dial is not turned to the desired position"):
        robot.move_gripper("around the dial") # make sure the gripper is still around the dial
        robot.turn_wrist("to the desired position") # turn the dial to the desired position.