# door-unlock: turn the dial on the door
def door_unlock(robot):
    # Steps
    #  1. Align the gripper with the dial
    #  2. Turn the dial clockwise to the correct position
    # If the gripper is not above the dial, move it above the dial
    if check("the robot's gripper is not above the dial"):
        robot.move_gripper("above the dial")
    # Close the gripper around the dial, if it's not closed already
    if check("the robot's gripper is not closed around the dial"):
        robot.move_gripper("around the dial", close_gripper=True)
    # Turn the dial clockwise until it's in the correct position
    dial_position = 0 # replace with the correct value
    while check("the dial is not in the correct position"):
        robot.turn_gripper_clockwise()
        dial_position += 1