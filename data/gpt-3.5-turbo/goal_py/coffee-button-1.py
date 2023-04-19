# Steps:
    #  1. Put gripper above the button
    #  2. Push down on the button
    # First, we need to move the gripper above the button.
    if check("the robot's gripper is not vertically aligned with the coffee button"):
        robot.move_gripper("vertically aligned with the coffee button")
    # Once the gripper is above the button, we can push down on it.
    if check("the robot's gripper is vertically aligned with the coffee button"):
        robot.move_gripper("near the coffee button")