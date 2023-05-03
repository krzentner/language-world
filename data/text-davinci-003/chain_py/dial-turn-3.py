
    # Steps:
    #  1. Put gripper above dial
    #  2. Line up gripper in front of dial
    #  3. Turn dial with gripper
    # First, we need to make sure the gripper is at least above the dial.
    if check("the robot's gripper is not above the dial and the robot's gripper is not vertically aligned with the dial"):
        robot.put("gripper above dial")
    # Try to line the gripper up with the dial as seen from the front.
    if check("the robot's gripper is almost forward aligned with the dial and the robot's gripper is not forward aligned with the dial"):
        robot.align("gripper to dial")
    # If the dial is lined up with the gripper, turn it.
    if check("the robot's gripper is forward aligned with the dial"):
        robot.turn("dial")