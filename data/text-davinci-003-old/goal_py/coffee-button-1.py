
    # Steps:
    #  1. Put gripper forward aligned with button
    #  2. Push button down
    # We need to start by putting the gripper forward aligned with the button.
    if check("the robot's gripper is not forward aligned with button"):
        robot.move_gripper("forward aligned with the button", close_gripper=True)
    # Once the gripper is lined up, push the button down.
    if check("the robot's gripper is forward aligned with button"):
        robot.move_gripper("near the button")