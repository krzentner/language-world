# Steps:
    #  1. Put gripper around the dial
    #  2. Turn dial to the correct code
    # To turn the dial, we need to grab onto the dial with the gripper.
    if check("the robot's gripper is not around the dial"):
        robot.move_gripper("around the dial", close_gripper=True)
    # Once the gripper is around the dial, we can turn it to the correct code.
    if check("the robot's gripper is around the dial"):
        robot.move_gripper("turned to the correct code")