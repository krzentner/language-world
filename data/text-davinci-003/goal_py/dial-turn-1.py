
    # Steps:
    #  1. Put gripper above the dial
    #  2. Grab the dial with the gripper
    #  3. Turn the dial
    # First, put the gripper above the dial.
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.move_gripper("vertically aligned with the dial")
    # If the gripper is above the dial, grab the dial by closing the gripper.
    if check("the robot's gripper is vertically aligned with the dial"):
        robot.move_gripper("above the dial", close_gripper=True)
    # If the gripper is already around the dial, rotate the dial to the left or right.
    if check("the robot's gripper is around the dial"):
        robot.move_gripper("left of the dial")