
    # Steps:
    #  1. Put gripper above the dial
    #  2. Put gripper around the dial
    #  3. Turn the dial to the left
    #  4. Turn the dial to the right
    # First, put the gripper above the dial.
    if check("the robot's gripper is not above the dial"):
        robot.put("gripper above dial")
    # When the gripper is above the dial, it should be easy to grab it by
    # moving the gripper around the dial.
    if check("the robot's gripper is above the dial and the robot's gripper is not around the dial"):
        robot.drop("gripper around dial")
    # Now that the gripper is around the dial, we can turn it to the left.
    if check("the robot's gripper is around the dial"):
        robot.turn("dial left")
    # Once the dial is turned to the left, we turn it to the right.
    if check("the dial is turned left"):
        robot.turn("dial right")