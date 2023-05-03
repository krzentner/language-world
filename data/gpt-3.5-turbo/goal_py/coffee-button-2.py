# Steps:
    #  1. Put gripper above the button
    #  2. Push the button
    # First, put the gripper above the button.
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Then, push the button by moving the gripper forward towards it.
    if check("the robot's gripper is vertically aligned with the button and not near it"):
        robot.move_gripper("near the button")