
    # Steps:
    #  1. Put gripper above the dial
    #  2. Grab the dial
    #  3. Turn the dial one full rotation
    # First, line the gripper up with the dial.
    if check("the robot's gripper is not above the dial"):
        robot.move_gripper("above the dial")
    # If the gripper isn't around the dial, put it around the dial.
    if check("the robot's gripper is not around the dial and the robot's gripper is open"):
        robot.move_gripper("close to the dial", close_gripper=True)
    # If the gripper closed around the dial, rotate the dial one full rotation.
    if check("the robot's gripper is around the dial and the robot's gripper is closed"):
        robot.move_gripper("full rotation")