# dial-turn: turn the dial to the specified combination
def dial_turn(robot, combination):
    # Steps:
    #  1. Put gripper around the dial handle
    #  2. Turn the dial to the first number
    #  3. Turn the dial to the second number
    #  4. Turn the dial to the third number
    # First, put the gripper around the dial handle.
    if check("the robot's gripper is not around the dial handle"):
        robot.drop("gripper around dial handle")
    # Turn the dial to the first number.
    if check(f"the robot's gripper is around the dial handle and the dial is not set to {combination[0]}"):
        robot.turn(f"dial to {combination[0]}")
    # Turn the dial to the second number.
    if check(f"the dial is not set to {combination[1]}"):
        robot.turn(f"dial to {combination[1]}")
    # Turn the dial to the third number.
    if check(f"the dial is not set to {combination[2]}"):
        robot.turn(f"dial to {combination[2]}")