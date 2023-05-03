

# dial-turn: turn the dial
def dial_turn(robot):
    # Steps:
    #  1. Put gripper above dial
    #  2. Line up the gripper with the dial
    #  3. Push the dial to turn it
    # First, put the gripper above the dial.
    if check("the robot's gripper is not vertically aligned with dial"):
        robot.put("gripper above dial")
    # Because the dial is a tall object, check if the gripper is near the side
    # of the dial instead of over it.
    if check("the robot's gripper is not forward aligned with the dial and the robot's gripper is not near the dial"):
        robot.grab("dial")
    # If the gripper is forward aligned with the dial and near it, we can turn
    # the dial.
    if check("the robot's gripper is forward aligned with the dial and the robot's gripper is near the dial"):
        robot.push("turn dial")