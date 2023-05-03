# Steps:
    #  1. Put gripper near the dial
    #  2. Turn the dial to lock the door
    # First, put the gripper next to the dial.
    if check("the robot's gripper is not near the dial"):
        robot.move_gripper("near the dial")
    # If the gripper is near the dial, we can turn it.
    if check("the robot's gripper is near the dial"):
        robot.move_gripper("around the dial", close_gripper=True)