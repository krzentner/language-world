# dial-turn: turn the dial
def dial_turn(robot):
    # Steps:
    #  1. Move the gripper roughly above the dial
    #  2. Grab the dial with the gripper
    #  3. Turn the dial
    # First, move the gripper roughly above the dial
    if check("the robot's gripper is not above the dial"):
        robot.move_gripper("above the dial")
    # If the gripper is above the dial, grab the dial
    if check("the robot's gripper is above the dial and the gripper is not around dial"):
        robot.move_gripper("around the dial")
    # Once the gripper is around the dial, turn the dial
    if check("the robot's gripper is around dial"):
        robot.move_gripper("horizontally aligned with the target dial position")