# dial: turn the dial to the specified number
def dial(robot, number):
    # Steps:
    #  1. Put gripper around the dial handle
    #  2. Turn dial to the correct number
    # First, put the gripper around the dial handle.
    if check("the robot's gripper is not around the dial handle"):
        robot.move_gripper("around the dial handle")
    # To turn the dial, we need to know which direction to turn it and how much.
    direction = "left" if number < robot.current_number else "right"
    amount = abs(number - robot.current_number)
    # Loop to turn the dial the required amount.
    for i in range(amount):
        # If we're at the correct number, we're done.
        if robot.current_number == number:
            break
        # Turn the dial once.
        robot.move_gripper(direction)
    # Update the robot's current number.
    robot.current_number = number

# door-lock: turn the dial on the door
def door_lock(robot):
    # Steps:
    #  1. Put gripper around the dial handle
    #  2. Turn the dial to the correct combination
    # First, put the gripper around the dial handle.
    if check("the robot's gripper is not around the dial handle"):
        robot.move_gripper("around the dial handle")
    # Turn the dial to the first number in the combination.
    dial(robot, robot.combination[0])
    # Turn the dial to the second number in the combination.
    dial(robot, robot.combination[1])
    # Turn the dial to the third number in the combination.
    dial(robot, robot.combination[2])
    # Turn the dial to the fourth number in the combination.
    dial(robot, robot.combination[3])
    # Once the correct combination is dialed in, the lock should open.