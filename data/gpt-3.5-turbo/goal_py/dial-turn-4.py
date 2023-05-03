# Steps:
    #  1. Put gripper around the dial
    #  2. Turn the dial to the desired position
    # First, put the gripper around the dial in a way that allows us to turn it.
    if check("the robot's gripper is not around the dial"):
        robot.move_gripper("around the dial")
    # Once the gripper is around the dial, we can turn it to the desired position.
    if check("the robot's gripper is around the dial"):
        robot.move_gripper("dial target position")