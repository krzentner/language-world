

The steps for the program should be:

1. Put gripper above the dial
2. Drop gripper around the dial
3. Turn the dial clockwise

# dial-turn: turn the dial
# def dial_turn(robot):
    # Steps:
    #  1. Put gripper above the dial
    #  2. Drop gripper around the dial
    #  3. Turn the dial clockwise
    # First, put the gripper above the dial, so that we make sure to grab it
    # correctly.
    if check("the robot's gripper is not above the dial"):
        robot.move_gripper("above the dial")
    # If the gripper is lined up roughly, make sure to move the gripper around
    # the dial to trap it.
    if check("the robot's gripper is not around dial and the robot's gripper is open"):
        robot.move_gripper("around the dial", close_gripper=True)
    # If the gripper is around the dial, we should be able to turn it clockwise
    # by moving the gripper.
    if check("the robot's gripper is around the dial"):
        robot.move_gripper("left of the dial")