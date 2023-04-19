# dial-turn: turn the dial
# def dial_turn(robot):
    # Steps:
    # 1. Put gripper above the dial
    # 2. Drop gripper around dial
    # 3. Turn dial to target position
    # First, put the gripper roughly above the dial so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the dial"):
        robot.move_gripper("above the dial")
    # If the gripper isn't around the dial, put it around the dial.
    if check("the robot's gripper is not around dial and the robot's gripper is open"):
        robot.move_gripper("near the dial", close_gripper=True)
    # If the gripper is around the dial and the dial's position is not aligned
    # with the target, turn the dial to the target position
    if check("the robot's gripper is around dial and the dial's position is not aligned with the target"):
        robot.move_gripper("aligned with the target position")