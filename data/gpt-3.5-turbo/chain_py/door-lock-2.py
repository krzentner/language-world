# Steps:
    #  1. Line up gripper with dial
    #  2. Grab the dial
    #  3. Turn the dial to the correct combination
    # First, put the gripper above the dial.
    if check("the robot's gripper is not above the lock dial"):
        robot.place("gripper above dial")
    # If the gripper isn't around the lock dial, grab it.
    if check("the robot's gripper is not around the lock dial and the robot's gripper is open"):
        robot.grab("lock dial")
    # If the gripper is around the lock dial, we can try turning it to the
    # correct combination.
    if check("the robot's gripper is around lock dial"):
        robot.turn("dial to correct combination")