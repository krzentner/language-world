# dial-right: turn the dial to the right to lock
def dial_right(robot):
    # Steps:
    #  1. Put gripper around dial
    #  2. Turn dial right
    # Because the dial is a small object, we need to be careful about its exact
    # position before we can turn it.
    # If the gripper is not around the dial, move it around the dial.
    if check("the robot's gripper is not around the dial"):
        robot.move_gripper("around the dial", close_gripper=True)
    # Once the gripper is around the dial, we can turn the dial right
    if check("the robot's gripper is around the dial"):
        robot.turn_dial("right")

# dial-left: turn the dial to the left to unlock
def dial_left(robot):
    # Steps:
    #  1. Put gripper around dial
    #  2. Turn dial left
    # Because the dial is a small object, we need to be careful about its exact
    # position before we can turn it.
    # If the gripper is not around the dial, move it around the dial.
    if check("the robot's gripper is not around the dial"):
        robot.move_gripper("around the dial", close_gripper=True)
    # Once the gripper is around the dial, we can turn the dial left
    if check("the robot's gripper is around the dial"):
        robot.turn_dial("left")