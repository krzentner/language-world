

Steps:
1. Put gripper above the dial
2. Drop gripper around the dial
3. Turn the dial to the correct position

# dial-turn: turn the dial
# def dial_turn(robot):
    # Steps:
    #  1. Put gripper above the dial
    #  2. Drop gripper around the dial
    #  3. Turn the dial to the correct position
    # If the robot's gripper is not near the dial, move the gripper above the dial.
    if check("the robot's gripper is not above the dial"):
        robot.put("gripper above dial")
    # Once the gripper is near the dial, drop down around it to grab it.
    if check("the robot's gripper is above the dial and the robot's gripper is open"):
        robot.drop("gripper around dial")
    # Once the gripper is around the dial, turn the dial in the correct direction.
    if check("the robot's gripper is around the dial"):
        robot.turn("dial to correct position")