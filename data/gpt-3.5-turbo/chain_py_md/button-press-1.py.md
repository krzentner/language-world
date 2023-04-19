# button-press: push the button from the front
# def button_press(robot):
    # Steps:
    #  1. Put gripper in front of button
    #  2. Close gripper around button
    #  3. Push button
    # Because this is "front", we need to put the gripper in front of the button.
    if check("the robot's gripper is not in front of the button"):
        robot.move("gripper to front of button")
    # Once the gripper is in front of the button, we can try to grab it by closing
    # the gripper around the button.
    if check("the robot's gripper is in front of button and the robot's gripper is open"):
        robot.close("gripper around button")
    # If we have a good grip on the button, push it.
    if check("the robot's gripper is around button"):
        robot.push("button")