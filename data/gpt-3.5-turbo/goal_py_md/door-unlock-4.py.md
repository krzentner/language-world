# door-unlock: turn the dial on the door
def door_unlock(robot):
    # Steps:
    #  1. Put gripper around the dial
    #  2. Turn the dial to the right
    #  3. Turn the dial to the left
    #  4. Turn the dial to the right until the door unlocks
    # First, put the gripper around the dial.
    if check("the robot's gripper is not around the door dial"):
        robot.move_gripper("around the door dial")
    # If the dial is not at the starting position, turn it all the way to the
    # left. We need to start from the same position every time, since we don't
    # know what position the dial is currently in.
    if check("the dial is not at the starting position"):
        robot.move_gripper("almost vertically aligned with the dial")
        robot.move_gripper("around the dial", close_gripper=True)
        robot.move_gripper("vertically aligned with the dial")
        robot.move_gripper("almost vertically aligned with the dial")
    # Turn the dial to the right.
    robot.move_gripper("horizontally aligned with the dial", close_gripper=True)
    robot.move_gripper("almost vertically aligned with the dial")
    # Turn the dial to the left.
    robot.move_gripper("horizontally aligned with the dial")
    robot.move_gripper("almost vertically aligned with the dial")
    # Turn the dial to the right until the door unlocks.
    while check("the door is still locked"):
        robot.move_gripper("horizontally aligned with the dial", close_gripper=True)
        robot.move_gripper("almost vertically aligned with the dial")