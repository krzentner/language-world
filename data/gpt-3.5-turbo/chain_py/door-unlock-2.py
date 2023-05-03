# Steps:
    #  1. Move gripper to dial
    #  2. Grab dial with gripper
    #  3. Move gripper to initial position for turning dial
    #  4. Turn the dial to the correct combination
    #  5. Move gripper back to initial position
    # If the robot's gripper is not near the dial, move it to the dial.
    if check("the robot's gripper is not near the dial"):
        robot.move("gripper to dial")
    # If the gripper is not around the dial, drop it around the dial.
    if check("the robot's gripper is not around the dial"):
        robot.drop("gripper around dial")
    # After the gripper is around the dial, move it to the initial position for
    # turning the dial.
    if check("the robot's gripper is around the dial and the robot's gripper is not in initial position for turning"):
        robot.move("gripper to initial position")
    # Once the gripper is in position, turn the dial to the correct combination.
    # If the dial is not already lined up correctly, move it to the first digit
    # of the combination.
    if check("the dial is not at the correct digit"):
        robot.turn("dial to correct digit")
    #Turn the dial to the second digit of the combination.
    if check("the first digit is correct and the dial is not at the correct digit"):
        robot.turn("dial to correct digit")
    # Turn the dial to the third digit of the combination.
    if check("the first and second digits are correct and the dial is not at the correct digit"):
        robot.turn("dial to correct digit")
    # After the correct combination is set, move the gripper back to initial
    # position.
    if check("the dial is at the correct digit and the robot's gripper is not in initial position"):
        robot.move("gripper to initial position")