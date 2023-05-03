# dial-turn: turn the dial
def dial_turn(robot):
    # Steps:
    #  1. Move gripper to the dial
    #  2. Rotate the dial to the desired position
    # Getting the gripper to the dial is similar to getting it to a door handle
    if check("the robot's gripper is not near the dial"):
        robot.move_gripper("near the dial")
    # Once the gripper is around the dial, we need to turn it to the desired
    # position
    if check("the robot's gripper is around the dial and the dial is not in the desired position"):
        robot.move_gripper("in position to turn the dial")