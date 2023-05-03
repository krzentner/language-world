# dial-turn: turn the dial
# def dial_turn(robot):
    # Steps:
    # 1. Align the gripper with the dial
    # 2. Put the gripper on the dial and pinch it
    # 3. Turn the dial to the required degree
    # 4. Release the dial
    # We need to line up the gripper with the dial before grabbing it.
    if check("the gripper is not aligned with the dial"):
        robot.put("gripper on top of the dial")
    # If the gripper is aligned with the dial and not holding it, pinch the dial.
    if check("the gripper is aligned with the dial and not holding it"):
        robot.pinch("the dial")
    # Once the gripper has held the dial, we can turn it to the required degree.
    if check("the gripper is holding the dial but not at the desired degree"):
        robot.turn("the dial to the required degree")
    # Finally, we release the dial.
    if check("the gripper is holding the dial"):
        robot.release("the dial")