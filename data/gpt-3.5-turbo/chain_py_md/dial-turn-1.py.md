# dial-turn: turn the dial
# def dial_turn(robot):
    # Steps:
    # 1. Move gripper to the dial
    # 2. Drop gripper around the dial
    # 3. Turn the dial to the desired position
    # First, put the gripper near the dial.
    if check("the robot's gripper is not near the dial"):
        robot.move("gripper to dial")
    # Once the gripper is near the dial, we can drop the gripper around it.
    if check("the robot's gripper is near the dial and the robot's gripper is open"):
        robot.drop("gripper around dial")
    # Once the gripper is around the dial, turn it to the desired position.
    if check("the robot's gripper is around the dial"):
        robot.turn("dial to the desired position")