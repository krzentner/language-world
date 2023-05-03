
    # Steps:
    #  1. Put gripper near dial
    #  2. Turn the dial
    # We can just move straight to the dial, no need to line up the gripper.
    if check("the robot's gripper is not near the dial"):
        robot.move_gripper("near the dial")
    # Once the gripper is near the dial, turn the dial.
    if check("the robot's gripper is near the dial"):
        robot.move_gripper("closer to the door")