# dial-turn: turn the dial
# def dial_turn(robot):
    # Steps:
    #  1. Put gripper near dial
    #  2. Turn the dial
    # First, put the gripper near the dial
    if check("the robot's gripper is not near the dial"):
        robot.move_gripper("near the dial")
    # Turn the dial by rotating the gripper
    if check("the robot's gripper is near the dial"):
        robot.rotate_gripper("clockwise", angle_in_degrees=90) # placeholder action, replace with actual code to turn the dial.