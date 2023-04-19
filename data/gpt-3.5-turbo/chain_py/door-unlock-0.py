# Steps:
    #  1. Put gripper around the dial
    #  2. Turn the dial to the correct combination
    # First, put the gripper around the dial.
    if check("the robot's gripper is not around the dial"):
        robot.drop("gripper around dial")
    # Turn the dial. We need to keep track of the current number, so we can
    # understand how far we've turned it.
    # We can't assume how many spins the dial takes to rotate or the direction
    # of rotation, so we'll need to experimentally figure that out and adjust
    # the steps accordingly.
    current_number = 0
    while current_number < combination[0]:
        robot.turn("dial right")
        current_number += 1
    while current_number > combination[0]:
        robot.turn("dial left")
        current_number -= 1
    # Repeat these steps for the second and third digits in the combination.
    current_number = 0
    while current_number < combination[1]:
        robot.turn("dial right")
        current_number += 1
    while current_number > combination[1]:
        robot.turn("dial left")
        current_number -= 1
    current_number = 0
    while current_number < combination[2]:
        robot.turn("dial right")
        current_number += 1
    while current_number > combination[2]:
        robot.turn("dial left")
        current_number -= 1
    # Once the dial is set to the correct combination, the door should unlock.
    robot.pull("door open")