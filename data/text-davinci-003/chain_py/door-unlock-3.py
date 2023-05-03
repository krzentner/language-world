
    # Steps:
    #  1. Put gripper above door dial
    #  2. Move down to dial
    #  3. Turn the dial clockwise
    #  4. Turn the dial counterclockwise
    # First, put the gripper above the door dial.
    if check("the robot's gripper is not above the door dial and the robot's gripper is not vertically aligned with the door dial"):
        robot.put("gripper above the door dial")
    # Once the gripper is above the door dial, drop it around the dial, so that
    # the robot can turn it.
    if check("the robot's gripper is not around the door dial"):
        robot.drop("gripper around the door dial")
    # Once the gripper is around the door dial, turn it clockwise.
    if check("the robot's gripper is around the door dial"):
        robot.turn("door dial clockwise")
    # After turning the dial clockwise, turn it counterclockwise.
    if check("the robot's gripper is around the door dial"):
        robot.turn("door dial counterclockwise")