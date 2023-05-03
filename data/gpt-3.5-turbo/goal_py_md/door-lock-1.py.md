# door-lock: turn the dial on the door
def door_lock(robot):
    # Steps:
    #  1. Put gripper around the dial
    #  2. Turn the dial to the correct combination
    #  3. If the door is unlocked, move the gripper away from the dial
    # If the gripper is not near the dial, move it close to the dial.
    if check("the robot's gripper is not around the dial"):
        robot.move_gripper("around the dial")
    # We need to rotate the dial to the correct combination to unlock the door.
    # Let's assume the combination is "12-34-56".
    combination = "12-34-56"
    current_combination = ""
    for i in range(len(combination)):
        # If the combination has been correctly set, stop turning the dial
        if current_combination == combination:
            break
        # Rotate the dial to the next number in the combination
        current_num = robot.read_dial()
        next_num = combination[i]
        while current_num != next_num:
            robot.rotate_dial("clockwise")
            current_num = robot.read_dial()
        # Add the current number to the current combination
        current_combination += current_num
    # If the correct combination has been set, move the gripper away from the
    # dial to indicate that the door is unlocked.
    if current_combination == combination:
        robot.move_gripper("away from the dial")