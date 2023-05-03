# Steps:
    #  1. Line up the gripper as viewed from the front
    #  2. Push the button from the front
    # We need to line up the gripper from the front rather than above.
    if check("the robot's gripper is not forward aligned with button"):
        robot.move_gripper("forward aligned with the button", close_gripper=True)
    # Once the gripper is in line with the button, push it from the front.
    if check("the robot's gripper is forward aligned with button"):
        robot.move_gripper("near the button")