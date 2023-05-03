# dial-turn: turn the dial
def dial_turn(robot):
    # Steps:
    #  1. Put gripper near the dial
    #  2. Turn the dial
    # To turn the dial, we need to move the robot's gripper near it.
    if check("the robot's gripper is not near the dial"):
        robot.move_gripper("near the dial")
    # Once the gripper is near the dial, we can turn it by closing the grip
    # around it and rotating the gripper.
    if check("the robot's gripper is near the dial"):
        robot.move_gripper("around the dial", rotate=True)