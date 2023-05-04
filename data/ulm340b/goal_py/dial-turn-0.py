
    # Steps:
    #  1. Put gripper above dial
    #  2. Close gripper around the dial
    #  3. Pull or push to turn the dial
    # Put the gripper above the dial.
    # Since we need to turn the dial clockwise, we need to put the robot's
    # gripper on its right side.
    if check("the robot's gripper is not above the dial"):
        robot.move_gripper("above the dial", close_gripper=True)
    # If the gripper is above the dial, close it to grab the dial.
    # The dial is large enough that the robot should be able to grab it from any
    # angle, so we don't need to be careful about aligning it.
    if check("the robot's gripper is above the dial"):
        robot.move_gripper("around the dial")
    # If the robot's gripper is around the dial, pull or push the dial to turn it.
    # Because we need to turn it clockwise, the robot should push the dial to
    # turn it.
    if check("the robot's gripper is around the dial"):
        robot.move_gripper("left of the dial")

# dial-turn-ccw: turn the dial counter-clockwise
def dial_turn_ccw(robot):
    # Steps:
    #  1. Put gripper above dial
    #  2. Close gripper around the dial
    #  3. Pull or push to turn the dial
    # Put the gripper above the dial.
    # Since we need to turn the dial counter-clockwise, we need to put the
    # robot's gripper on its left side.
    if check("the robot's gripper is not above the dial"):
        robot.move_gripper("above the dial", close_gripper=True)
    # If the gripper is above the dial, close it to grab the dial.
    # The dial is large enough that the robot should be able to grab it from any
    # angle, so we don't need to be careful about aligning it.
    if check("the robot's gripper is above the dial"):
        robot.move_gripper("around the dial")
    # If the robot's gripper is around the dial, pull