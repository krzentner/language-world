
    # Steps:
    #  1. Line up the gripper as viewed from in front
    #  2. Push down on the button from in front
    # To push the button from the front, we just need to line up the gripper.
    # Line up the robot's gripper from the front.
    if check("the robot's gripper is not forward aligned with button"):
        robot.move_gripper("forward aligned with the button", close_gripper=True)
    # Now that the gripper is almost lined up, push down on the button from the
    # front.
    if check("the robot's gripper is forward aligned with button"):
        robot.move_gripper("near the button")