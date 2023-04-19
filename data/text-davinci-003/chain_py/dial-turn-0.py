
    # Steps:
    #  1. Put gripper above the dial
    #  2. Grab the dial
    #  3. Rotate the dial to the desired position
    # We need to put the gripper above the dial so that we don't bump it with
    # the gripper.
    if check("the robot's gripper is not above the dial"):
        robot.put("gripper above dial")
    # After we've moved the gripper above the dial, we can grab the dial.
    if check("the robot's gripper is above the dial and the robot's gripper is open"):
        robot.grab("dial")
    # If we can grab the dial and the gripper is closed, then we can rotate the
    # dial to our desired position.
    if check("the robot's gripper is around the dial"):
        robot.rotate("dial to desired position")