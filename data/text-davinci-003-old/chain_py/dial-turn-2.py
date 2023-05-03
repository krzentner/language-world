
    # Steps:
    #  1. Put gripper above the dial
    #  2. Put gripper around dial
    #  3. Turn the dial
    # Put the gripper above the dial so the gripper is lined up with the dial.
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.put("gripper above dial")
    # If the gripper is lined up with the dial and not around it, put the
    # gripper around the dial.
    if check("the robot's gripper is vertically aligned with the dial and the robot's gripper is not around dial"):
        robot.grab("dial")
    # Once the gripper is around the dial, turn the dial.
    if check("the robot's gripper is around dial"):
        robot.rotate("dial")