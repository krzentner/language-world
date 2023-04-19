# dial-turn: turn the dial
# def dial_turn(robot):
    # Steps:
    #  1. Put gripper above the dial
    #  2. Grab the dial with the gripper
    #  3. Turn the dial to the desired position
    # First, put the gripper above the dial.
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.move_gripper("vertically aligned with the dial")
    # If the gripper is not around the dial grab it.
    if check("the robot's gripper is not around the dial and the robot's gripper is open"):
        robot.move_gripper("near the dial", close_gripper=True)
    # If the gripper is near the dial, turn the dial to the desired position.
    if check("the robot's gripper is near dial and the gripper is closed"):
        robot.move_gripper("at the desired position relative to the current position")