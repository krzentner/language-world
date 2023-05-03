# dial-turn: turn the dial
def dial_turn(robot):
    # Steps:
    #  1. Put gripper above the dial
    #  2. Grab the dial with the gripper
    #  3. Turn the dial to the desired position
    # First, put the gripper above the dial.
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.put("gripper above the dial")
    # If the dial isn't between the gripper fingers, we need to grab it.
    if check("the dial is not between the robot's gripper fingers"):
        robot.grab("the dial")
    # Once the dial is between the gripper fingers, we can turn it.
    if check("the dial is between the robot's gripper fingers"):
        robot.turn("the dial to the desired position")