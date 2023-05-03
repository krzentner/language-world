

# dial-turn: turn the dial
# def dial_turn(robot):
    # Steps:
    #  1. Put gripper directly above the dial
    #  2. Drop gripper around the dial
    #  3. Turn the dial
    # First, we need to put the robot's gripper directly above the dial.
    if check("the robot's gripper is not directly above the dial"):
        robot.move_gripper("directly above the dial")
    # Now that the gripper is above the dial, drop the gripper around it to
    # hold and turn it.
    if check("the robot's gripper is not around the dial"):
        robot.move_gripper("near the dial", close_gripper=True)
    # While holding the dial, we can turn it to the desired position.
    if check("the robot's gripper is around the dial"):
        robot.move_gripper("close to the desired position")