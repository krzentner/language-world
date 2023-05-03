# dial-turn: turn the dial
# def dial_turn(robot):
    # Steps:
    #  1. Put gripper above the dial
    #  2. Grab the dial
    #  3. Turn the dial to the desired position
    # First, put the gripper above the dial.
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.put("gripper above the dial")
    # Once the gripper is roughly above the dial, we can try to grab it.
    if check("the robot's gripper is above the dial and the robot's gripper is open"):
        robot.drop("gripper around the dial")
    # If the gripper is closed and around the dial, turn it to the desired position.
    if check("the robot's gripper is around the dial"):
        robot.turn("the dial to the desired position")