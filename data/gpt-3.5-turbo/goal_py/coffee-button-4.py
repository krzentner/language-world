# Steps:
    #  1. Put the gripper above the button
    #  2. Push the button
    # First, put the gripper above the button.
    if check("the robot's gripper is not vertically aligned with the coffee button"):
        robot.move_gripper("vertically aligned with the coffee button", close_gripper=True)
    # Once the gripper is lined up, push the button.
    if check("the robot's gripper is vertically aligned with the coffee button"):
        robot.move_gripper("near the coffee button")