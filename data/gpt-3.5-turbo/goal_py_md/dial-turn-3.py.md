# dial-turn: turn the dial
# def dial_turn(robot):
    # Steps:
    #  1. Put gripper near the dial
    #  2. Turn the dial
    # First, put the gripper near the dial.
    if check("the robot's gripper is not near the dial"):
        robot.move_gripper("near the dial")
    # If the gripper is near the dial, turn the dial.
    if check("the robot's gripper is near the dial"):
        robot.rotate_gripper("clockwise") # Or counterclockwise if turning the other way.