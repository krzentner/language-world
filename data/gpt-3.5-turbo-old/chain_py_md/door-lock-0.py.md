# door-lock: turn the dial on the door
# def door_lock(robot):
    # Steps:
    #  1. Put gripper around the dial
    #  2. Turn the dial to the right until it clicks
    #  3. Turn the dial to the left until it clicks again
    # First, position the gripper around the dial. 
    if check("the robot's gripper is not around the door lock dial"):
        robot.grab("door lock dial")
    # Turn the dial to the right until it clicks
    while check("the dial has not clicked yet"):
        robot.turn("dial to the right")
    # After the dial clicks to the right, turn it to the left until it clicks again
    while check("the dial has not clicked again"):
        robot.turn("dial to the left")