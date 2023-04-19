
    # Steps:
    #  1. Put gripper in front of the button
    #  2. Push the button
    # If the robot's gripper is not in front of the button, move the gripper
    # in front of the button.
    if check("the robot's gripper is not in front of the button"):
        robot.move("gripper in front of button")
    # If the robot's gripper is in front of the button, push the button.
    if check("the robot's gripper is in front of the button"):
        robot.push("button")