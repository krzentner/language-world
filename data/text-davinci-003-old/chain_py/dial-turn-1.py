
    # Steps:
    #  1. Get the robot's gripper around the dial
    #  2. Turn the dial
    # If the robot's gripper is not over the dial, it needs to be moved up and
    # sideways so that it can grab the dial.
    if check("the robot's gripper is not above the dial and the robot's gripper is not horizontally aligned with the dial"):
        robot.put("gripper above dial")
    # After the gripper is over the dial, it's just a matter of trapping it and
    # turning it.
    # Move the gripper down around the dial and close it to trap the dial.
    if check("the robot's gripper is above the dial and the robot's gripper is not around the dial and the robot's gripper is open"):
        robot.grab("dial")
    # Now that the dial is trapped, just turn it.
    if check("the robot's gripper is around the dial and the robot's gripper is closed"):
        robot.turn("dial clockwise")