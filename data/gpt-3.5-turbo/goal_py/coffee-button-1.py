# Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Put the gripper down on the button
    # We don't need to move the gripper much for this task.
    # Line up the gripper from above.
    if check("the robot's gripper is not vertically aligned with coffee button"):
        robot.move_gripper("vertically aligned with the coffee button", close_gripper=True)
    # Put the gripper down on the button and then lift it up again.
    if check("the robot's gripper is vertically aligned with coffee button"):
        robot.move_gripper("on top of the coffee button")
        robot.move_gripper("vertically aligned with the coffee button")