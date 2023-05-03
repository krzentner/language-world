
    # Steps:
    #  1. Put gripper above dial
    #  2. Move gripper around dial
    #  3. Rotate dial clockwise
    # To start, put the robot's gripper above dial.
    if check("the robot's gripper is not vertically aligned with dial"):
        robot.put("gripper above dial")
    # Once the gripper is above the dial, place it around the dial.
    if check("the robot's gripper is vertically aligned with dial and the robot's gripper is open"):
        robot.put("gripper around dial")
    # Once the gripper is around the dial, we can turn the dial clockwise.
    if check("the robot's gripper is around dial"):
        robot.turn("dial clockwise")