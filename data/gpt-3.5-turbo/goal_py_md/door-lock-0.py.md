# door-lock: turn the dial on the door
def door_lock(robot):
    # Steps:
    #  1. Move gripper to the dial
    #  2. Turn the dial to the correct combination
    
    # Move the gripper to the dial.
    if check("the robot's gripper is not near the door dial"):
        robot.move_gripper("near the door dial")
    
    # Turn the dial to the correct combination.
    # Assume that we know the 3-number combination, and perform
    # the following steps:
    #  1. Turn the dial clockwise to the first number.
    #  2. Turn the dial counterclockwise to the second number.
    #  3. Turn the dial clockwise to the third number.
    robot.turn_dial("clockwise", 10) # turn dial 10 units clockwise
    robot.turn_dial("counterclockwise", 5) # turn dial 5 units counterclockwise
    robot.turn_dial("clockwise", 8) # turn dial 8 units clockwise