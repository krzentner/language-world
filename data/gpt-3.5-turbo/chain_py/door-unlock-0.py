# Steps:
    #  1. Put gripper around the dial
    #  2. Turn the dial to the correct combination
    # First, put the gripper around the dial.
    if check("the robot's gripper is not around the dial"):
        robot.drop("gripper around dial")
    # Then, turn the dial to the correct combination.
    if check("the robot's gripper is around the dial"):
        robot.rotate("dial to unlock the door")