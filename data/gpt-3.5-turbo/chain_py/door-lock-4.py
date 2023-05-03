# Steps:
    #  1. Put gripper around the dial
    #  2. Turn dial to the correct combination
    #  3. Lock the door
    # First, put the gripper around the dial.
    if check("the robot's gripper is not around the dial"):
        robot.drop("gripper around dial")
    # Turn the dial to the correct combination.
    if check("the dial is not set to the correct combination"):
        robot.turn("the dial to the correct combination")
    # Lock the door by turning the dial to the lock position.
    if check("the dial is set to the correct combination"):
        robot.turn("the dial to lock the door")