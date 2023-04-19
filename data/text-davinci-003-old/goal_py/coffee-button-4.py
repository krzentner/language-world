
    # Steps:
    #  1. Put gripper above the button
    #  2. Push the button
    # First, put the gripper above the button.
    if check("the robot's gripper is not above the button"):
        robot.move_gripper("above the button")
    # Once the gripper is above the button, we can just push it.
    if check("the robot's gripper is above the button"):
        robot.move_gripper("near the button", close_gripper=True)