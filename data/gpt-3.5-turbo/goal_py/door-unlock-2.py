# dial-start: move the gripper to the start position for turning the dial
def dial_start(robot):
    # Steps:
    #  1. Put gripper left of the dial
    #  2. Move gripper down to the dial
    #  3. Line up the gripper with the dial
    # The first step is to move the gripper to the left of the dial.
    if check("the robot's gripper is not left of the dial"):
        robot.move_gripper("left of the dial")
    # Once the gripper is to the left of the dial, move it down towards the dial.
    if check("the robot's gripper is left of the dial and not vertically aligned with the dial"):
        robot.move_gripper("vertically aligned with the dial")
    # Now that the gripper is above the dial, we need to line it up with the
    # dial to be able to turn it.
    if check("the robot's gripper is not horizontally aligned with the dial"):
        robot.move_gripper("horizontally aligned with the dial")

# dial-turn: turn the dial by a specified number of ticks
def dial_turn(robot, num_ticks):
    # Steps:
    #  1. A single tick typically takes about X seconds
    #  2. Turn the dial by the specified number of ticks using the arm's rotation
    #     functionality
    # To turn the dial, we'll rotate the entire arm by a certain number of degrees.
    ticks_to_degrees = num_ticks * 360 / 40  # assume 40 ticks per rotation
    robot.rotate_arm(ticks_to_degrees)

# dial-finish: move the gripper away from the dial
def dial_finish(robot):
    # Steps:
    #  1. Move gripper up and away from the dial
    # After turning the dial, we need to move the gripper away from the dial to
    # avoid accidentally bumping it.
    if check("the robot's gripper is not vertically aligned with the start position for turning the dial"):
        robot.move_gripper("vertically aligned with the start position for turning the dial")
    if check("the robot's gripper is vertically aligned with the start position for turning the dial and not above the dial"):
        robot.move_gripper("above the dial")