

# button-press: push the button from the front
# def button_press(robot):
    # Steps:
    #  1. Move the robot's gripper to the button
    #  2. Push down on the button
    # First, the robot's gripper should be moved to the button. 
    if check("the robot's gripper is not near the button"):
        robot.move("gripper to button")
    # Once the gripper is near the button, push down on it.
    if check("the robot's gripper is near the button"):
        robot.push("down on button")