
    # Steps:
    #  1. Put gripper above dial
    #  2. Grab the dial with the gripper
    #  3. Turn the dial
    # If the gripper is not near the dial, move it to the dial.
    if check("the robot's gripper is not near the dial"):
        robot.move("gripper to the dial")
    # If the gripper is near the dial but not touching it, grab the dial to
    # trap it.
    if check("the robot's gripper is near the dial and the robot's gripper is open"):
        robot.grab("dial")
    # If the gripper has the dial trapped, turn it to the desired location.
    if check("the robot's gripper is around the dial and the robot's gripper is closed"):
        robot.turn("dial to desired location")