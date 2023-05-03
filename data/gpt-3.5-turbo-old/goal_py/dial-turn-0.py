# Steps:
    #  1. Put gripper around the dial
    #  2. Turn the dial to the desired position
    #  3. Release the dial
    # First, put the gripper roughly around the dial.
    if check("the robot's gripper is not roughly around the dial and the gripper is open"):
        robot.move_gripper("around the dial", close_gripper=True)
    # Once the gripper is around the dial, turn the dial to the desired position.
    # We can do this by simply moving the gripper in a circular motion.
    if check("the robot's gripper is around the dial"):
        robot.move_gripper("around the dial in a circular motion")
    # Once the dial is turned to the desired position, release it by opening
    # the gripper again.
    if check("the dial is in the desired position"):
        robot.move_gripper("around the dial", close_gripper=False)