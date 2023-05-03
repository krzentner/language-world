
    # Steps:
    #  1. Gripper aligned from above
    #  2. Drop the gripper around dial
    #  3. Turn dial
    # We need to be careful about lining up the gripper with the dial, because
    # the dial is small.
    # Line up the gripper with the dial from above.
    if check("the robot's gripper is not horizontally and vertically aligned with dial"):
        robot.put("gripper above dial")
    # If the gripper is almost lined up, just line it up the rest of the way by
    # closing the gripper around the dial.
    if check("the robot's gripper is almost horizontally and vertically aligned with dial and the robot's gripper is open"):
        robot.close("gripper around dial")
    # Once the gripper is around the dial, we can turn it, so try to turn it in
    # the right direction.
    if check("the robot's gripper is horizontally and vertically aligned with dial and the robot's gripper is closed"):
        robot.turn("dial")