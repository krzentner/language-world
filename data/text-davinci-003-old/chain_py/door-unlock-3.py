
    # Steps:
    #  1. Put gripper above the dial
    #  2. Drop the gripper around the dial
    #  3. Spin the dial in the correct direction
    # First, we need to put the gripper above the dial in order to grab it.
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.put("gripper above dial")
    # If the gripper is around the dial and not closed, close the gripper so
    # that it holds the dial.
    if check("the robot's gripper is around dial and the robot's gripper is not closed"):
        robot.grab("dial")
    # If the gripper is closed around the dial, spin it in the right direction.
    if check("the robot's gripper is closed around the dial"):
        robot.spin("dial in direction to open door")