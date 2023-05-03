# dial-turn: turn the dial
def dial_turn(robot):
    # Steps:
    #  1. Move the gripper to the dial
    #  2. Turn the dial
    # The robot needs to move its gripper to the dial before it can turn it.
    # If the dial is not aligned with the robot's gripper from the front, move
    # the gripper to roughly above the dial.
    if check("the robot's gripper is not above the dial and the dial is not forward aligned with the robot's gripper"):
        robot.move_gripper("above the dial")
    # Once the gripper is above the dial, turn the dial.
    if check("the robot's gripper is above the dial"):
        robot.move_gripper("around the dial")