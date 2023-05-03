
    # Steps:
    #  1. Put gripper above button
    #  2. Drop gripper around button
    #  3. Push the button down
    # We'd like the robot to be able to push the button from any direction, so
    # we're just going to move its gripper above the button.
    # We don't need to be careful about the direction, since we're just pushing
    # it.
    if check("the robot's gripper is not above button"):
        robot.move_gripper("above the button")
    # Once the gripper is above the button, we can just move it down to push
    # it.
    if check("the robot's gripper is above button"):
        robot.move_gripper("below the button", close_gripper=True)