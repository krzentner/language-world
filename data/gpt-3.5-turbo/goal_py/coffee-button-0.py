# Steps:
    #  1. Put gripper above the button
    #  2. Push the button
    # We just need to put the gripper above the button and push it.
    # First, line up the gripper vertically with the button.
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Once the gripper is lined up, move it near the button and push it.
    if check("the robot's gripper is vertically aligned with the button"):
        robot.move_gripper("near the button")