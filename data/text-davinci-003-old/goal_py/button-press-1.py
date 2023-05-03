
    # Steps:
    #  1. Put gripper in front of the button
    #  2. Push the button
    # We need to put the gripper in front of the button before we can press it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not forward aligned with button"):
        robot.move_gripper("forward aligned with the button", close_gripper=True)
    # Once the gripper is lined up in front of the button, we should be able to
    # push the button by pushing down on it.
    if check("the robot's gripper is forward aligned with the button"):
        robot.move_gripper("near the button")