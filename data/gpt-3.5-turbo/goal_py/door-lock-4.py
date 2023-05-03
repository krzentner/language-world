# Steps:
    #  1. Put gripper around the dial
    #  2. Turn the dial to the correct combination
    # We need to put the gripper around the dial before we can turn it.
    if check("the robot's gripper is not around the dial"):
        robot.move_gripper("around the dial")
    # Once the gripper is around the dial, we can begin turning it to the
    # correct combination.
    if check("the robot's gripper is around the dial"):
        robot.move_gripper("turning the dial")