
    # Steps:
    #  1. Put gripper above the door lock's dial
    #  2. Grab lock's dial with gripper
    #  3. Turn the dial
    # Put the gripper vertically above the dial.
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.move_gripper("vertically aligned with the dial")
    # once the gripper is above the dial, it can pull down to grab the dial.
    if check("the robot's gripper is not above the dial"):
        robot.move_gripper("above the dial", close_gripper=True)
    # If the gripper is now around the dial, we should be able to turn the
    # dial.
    if check("the robot's gripper is around the dial"):
        robot.move_gripper("left of the dial")