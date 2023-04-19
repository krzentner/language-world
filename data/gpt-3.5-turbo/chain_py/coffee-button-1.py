# Steps:
    #  1. Align the gripper with the button
    #  2. Push down on the button
    # First, put the gripper in the position to push the button.
    if check("the robot's gripper is not aligned with the button"):
        robot.align("gripper with button")
    # Once the gripper is aligned with the button, push down on the button.
    if check("the robot's gripper is aligned with the button"):
        robot.push("down on button")