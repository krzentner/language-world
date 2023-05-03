
    # Steps:
    #  1. Turn the dial clockwise
    #  2. Turn the dial 90 degrees
    #  3. Turn the dial counterclockwise
    # Put the gripper in front of the door handle.
    if check("the robot's gripper is not in front of the door handle"):
        robot.move_gripper("in front of the door handle")
    # We can turn the dial by turning the gripper.
    if check("the robot's gripper is in front of the door handle"):
        robot.turn_gripper("clockwise")
    # Turn the dial 90 degress.
    if check("the door handle is not at 90 degrees turned"):
        robot.turn_gripper("90 degrees")
    # Turn the dial counterclockwise.
    if check("the door handle is at 90 degrees turned"):
        robot.turn_gripper("counterclockwise")