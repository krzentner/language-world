# Steps:
    #  1. Move gripper near the dial
    #  2. Grab the dial with the gripper
    #  3. Turn the dial to the correct combination
    #  4. Release the dial
    # First, move the gripper near the dial.
    if check("the robot's gripper is not near the dial"):
        robot.move_gripper("near the dial")
    # Once the gripper is near the dial, grab it with the gripper and turn the dial.
    if check("the robot's gripper is near the dial and the gripper is not grabbing the dial"):
        robot.move_gripper("around the dial", close_gripper=True)
        robot.turn_dial()
    # Release the dial by opening the gripper.
    if check("the robot's gripper is around the dial"):
        robot.move_gripper("right of the dial", close_gripper=False)