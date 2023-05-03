# door-lock: turn the dial on the door
def door_lock(robot):
    # Steps:
    #  1. Put gripper around dial
    #  2. Turn the dial to the correct combination
    # First, line up the gripper around the dial.
    if check("the robot's gripper is not around the dial"):
        robot.move_gripper("around the dial")
    # Once the gripper is around the dial, turn the dial to the correct
    # combination.
    # The direction to turn the dial and the number of ticks to turn it are
    # specific to the lock and the combination that needs to be entered.
    # Therefore, this part of the code needs to be customized for each lock and
    # combination.
    robot.turn_dial("clockwise", 7)
    robot.turn_dial("counterclockwise", 3)
    robot.turn_dial("clockwise", 5)
    robot.turn_dial("counterclockwise", 1)