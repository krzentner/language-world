# Steps:
    #  1. Put gripper above the dial
    #  2. Grab the dial with the gripper
    #  3. Turn the dial counterclockwise to unlock
    # First, put the gripper above the dial.
    if check("the robot's gripper is not above the dial"):
        robot.put("gripper above the dial")
    # Once the gripper is above the dial, grab it.
    if check("the robot's gripper is above the dial and the robot's gripper is open"):
        robot.grab("the dial")
    # Once the gripper is around the dial, turn it counterclockwise to the
    # unlock position.
    if check("the robot's gripper is around the dial"):
        robot.turn("the dial counterclockwise to unlock position")