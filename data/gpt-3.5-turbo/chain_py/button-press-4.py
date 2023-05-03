# Steps:
    #  1. Move gripper left of button
    #  2. Push the button forwards
    # Because this is "front", we need to move the gripper left of the button
    # before pushing it forwards.
    # Move the gripper left of the button.
    if check("the robot's gripper is not left of button"):
        robot.move("gripper to left of button")
    # Once the gripper is left of the button, push the button forwards.
    if check("the robot's gripper is left of button"):
        robot.push("button forwards")