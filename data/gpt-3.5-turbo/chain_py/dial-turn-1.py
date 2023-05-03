# Steps:
    #  1. Put gripper around dial
    #  2. Turn dial to desired position
    # We need to be careful to grab the dial with the gripper, since it's small
    # and we can't just push it around.
    # If the gripper is not around the dial, put it around the dial.
    if check("the robot's gripper is not around the dial and the robot's gripper is open"):
        robot.drop("gripper around dial")
    # Once the gripper is around the dial, we can turn the dial to the desired
    # position.
    if check("the robot's gripper is around dial"):
        robot.turn("dial to desired position")