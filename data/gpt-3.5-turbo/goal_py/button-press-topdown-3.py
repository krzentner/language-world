# Steps:
    #  1. Put gripper above button
    #  2. Drop gripper around the button
    #  3. Push down on the button
    # First, put the gripper above the button.
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.move_gripper("vertically aligned with the button")
    # If the gripper is not around the button, put it around the button.
    if check("the robot's gripper is not around button and the robot's gripper is open"):
        robot.move_gripper("above the button", close_gripper=True)
    # If the gripper is around the button, push down on the button.
    if check("the robot's gripper is around button"):
        robot.move_gripper("vertically aligned with the button")