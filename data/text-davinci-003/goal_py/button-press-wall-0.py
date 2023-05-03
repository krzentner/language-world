
    # Steps:
    #  1. Line up the gripper as viewed from the front
    #  2. Push down on the button
    # Because of the wall in the way, we can't line up the gripper just above the
    # button.
    # Line up the robot's gripper from the front.
    if check("the robot's gripper is not forward aligned with the button"):
        robot.move_gripper("close to the button from the front")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is close to the button from the front"):
        robot.move_gripper("around the button")