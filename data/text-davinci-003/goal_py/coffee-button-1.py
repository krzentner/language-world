
    # Steps:
    #  1. Put gripper close to the button
    #  2. Push the button down
    # We need to put the gripper close to the button so that when we push the
    # button down, it doesn't bounce back up again.
    if check("the robot's gripper is not close to the button"):
        robot.move_gripper("close to the button")
    # Once the gripper is close enough to the button, we just need to push it
    # down.
    if check("the robot's gripper is close to the button"):
        robot.move_gripper("above the button", close_gripper=True)