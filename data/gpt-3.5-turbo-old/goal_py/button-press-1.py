    # Steps:
    #  1. Line up the gripper as viewed from the front
    #  2. Push the button from the front
    # To press the button from the front, we need to first line up the gripper
    # correctly.
    if check("the robot's gripper is not forward aligned with button"):
        robot.move_gripper("forward aligned with the button")
    # Once the gripper is lined up, we can just push the button.
    if check("the robot's gripper is forward aligned with button"):
        robot.move_gripper("near the button")