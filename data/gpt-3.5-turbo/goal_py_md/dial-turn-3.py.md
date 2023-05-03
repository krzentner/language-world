# dial-turn: turn the dial
def dial_turn(robot):
    # Steps:
    #  1. Put gripper around the dial
    #  2. Get a good grip on the dial
    #  3. Turn the dial
    # First, put the gripper around the dial.
    if check("the robot's gripper is not around dial"):
        robot.move_gripper("around the dial")
    # Once the gripper is around the dial, we need to get a good grip on it.
    # Close the gripper to ensure that we are holding the dial firmly.
    if check("the robot's gripper is around dial and the robot's gripper is open"):
        robot.move_gripper("around the dial", close_gripper=True)
    # Now that we have a good grip on the dial, we can turn it.
    # We can use the gripper to apply pressure to the dial in order to turn it.
    if check("the robot's gripper is around dial and the gripper is firmly holding the dial"):
        robot.move_gripper("around the dial", apply_pressure=True)