
    # Steps:
    #  1. Put gripper above the dial
    #  2. Drop gripper around the dial
    #  3. Turn the dial
    # First, put the gripper above the dial.
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.put("gripper above dial")
    # We should be able to grab the top of the dial by moving the gripper
    # around.
    if check("the robot's gripper is vertically aligned with the dial and the robot's gripper is open"):
        robot.put("gripper around dial")
    # If the gripper is successfully gripping the top of the dial and still
    # vertically aligned, turn the dial slightly.
    if check("the robot's gripper is forward aligned with dial"):
        robot.turn("dial")