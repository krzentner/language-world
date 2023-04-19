# button-press: push the button from the front
# def button_press(robot):
    # Steps:
    #  1. Put gripper in front of button 
    #  2. Push the button
    # The robot needs to position the gripper in front of the button, and then
    # push it straight in.
    # If the gripper is not in front of the button, move the gripper in front
    if check("the robot's gripper is not in front of the button"):
        robot.put("gripper in front of button")
    # Once the gripper is in front of the button, push the button
    if check("the robot's gripper is in front of the button"):
        robot.push("button")