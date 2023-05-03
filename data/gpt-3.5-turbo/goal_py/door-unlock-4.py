# dial: turn the dial
def dial(robot):
    # Steps:
    #  1. Put the gripper around the dial
    #  2. Turn the dial to the correct position (if not already there)
    # We assume that the gripper is already near the dial.
    # If the gripper is not around the dial, put it around the dial.
    if check("the robot's gripper is not around the dial"):
        robot.move_gripper("around the dial")
    # If the dial is not already at the correct position, turn it.
    if check("the dial is not at the correct position"):
        robot.move_gripper("to the correct position")