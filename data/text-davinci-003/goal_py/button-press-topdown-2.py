
    # Steps:
    #  1. Put gripper above button
    #  2. Drop gripper on top of button
    #  3. Push down on the button
    # We want to make sure the gripper is above the button before it starts
    # dropping down, so that it doesn't miss the button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with button")
    # If the gripper is lined up above the button and it's not resting on the
    # button, drop gripper on top of the button.
    # We don't want to close the gripper here, because we don't want to lose the
    # button in the gripper.
    if check("the robot's gripper is not on top of the button and the robot's gripper is vertically aligned with button"):
        robot.move_gripper("on top of the button")
    # Once the gripper is on top of the button, we can press the button.
    if check("the robot's gripper is on top of the button"):
        robot.move_gripper("downward on the button")