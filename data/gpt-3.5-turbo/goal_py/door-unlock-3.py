# dial-left: turn the dial counter-clockwise
def dial_left(robot):
    # Steps:
    #  1. Put gripper around dial
    #  2. Turn the dial counter-clockwise
    # First, put the gripper around the dial.
    if check("the robot's gripper is not around the dial and the robot's gripper is not near the dial"):
        robot.move_gripper("near the dial", close_gripper=True)
    # Once the gripper is around the dial, turn it counter-clockwise.
    if check("the robot's gripper is around the dial"):
        robot.move_gripper("turn counter-clockwise")

# dial-right: turn the dial clockwise
def dial_right(robot):
    # Steps:
    #  1. Put gripper around dial
    #  2. Turn the dial clockwise
    # First, put the gripper around the dial.
    if check("the robot's gripper is not around the dial and the robot's gripper is not near the dial"):
        robot.move_gripper("near the dial", close_gripper=True)
    # Once the gripper is around the dial, turn it clockwise.
    if check("the robot's gripper is around the dial"):
        robot.move_gripper("turn clockwise")