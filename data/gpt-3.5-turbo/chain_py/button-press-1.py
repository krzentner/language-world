# Steps:
    #  1. Move gripper to left of button
    #  2. Move gripper forward until it presses the button
    #  3. Push down on the button
    # For this task, we need to move the gripper into a position where it can push
    # the button from the front.
    # First, move the gripper to the left of the button.
    if check("the robot's gripper is not left of the button"):
        robot.move("gripper to left of button")
    # If the gripper is left of the button but not forward enough to press it,
    # move the gripper forward until it presses the button.
    if check("the robot's gripper is left of the button but not pressing the button"):
        robot.move("gripper forward until it presses the button")
    # Once the gripper is pressing the button, push down on the button.
    if check("the robot's gripper is pressing the button"):
        robot.push("down on button")