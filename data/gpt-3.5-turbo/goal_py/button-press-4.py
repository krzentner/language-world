# Steps:
    #  1. Put gripper in front of button
    #  2. Push button from the front
    # First, move the gripper in front of the button.
    if check("the robot's gripper is not in front of button"):
        robot.move_gripper("in front of the button")
    # Once the gripper is in front of the button, push it.
    if check("the robot's gripper is in front of the button"):
        robot.move_gripper("near the button")