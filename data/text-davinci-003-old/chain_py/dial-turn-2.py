
    # Steps:
    #  1. Put gripper above the dial
    #  2. Drop gripper around the dial
    #  3. Turn the dial
    # First, put the gripper above the dial.
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.put("gripper above dial")
    # If the gripper is not around the dial, put it around the dial.
    # We don't need to be careful about the direction, since the dial is small
    # and we're just turning it.
    if check("the robot's gripper is not around dial and the robot's gripper is open"):
        robot.grab("dial")
    # Once the gripper is around the dial, we can just turn the dial.
    if check("the robot's gripper is around dial"):
        robot.turn("dial")