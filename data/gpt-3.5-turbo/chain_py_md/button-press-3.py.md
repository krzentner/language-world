# button-press: push the button from the front
def button_press(robot):
    # Steps:
    # 1. Put the gripper in front of the button
    # 2. Move the gripper down onto the button
    # 3. Push the button
    # As this is "front-facing", we need to put the gripper in front of the 
    # button.
    if check("the robot's gripper is not in front of button"):
        robot.move("gripper in front of button")
    # Once the gripper is in front of the button, we should move it down onto
    # the button to push it.
    if check("the robot's gripper is in front of button and the robot's gripper is not touching the button"):
        robot.put("gripper on the button")
    # Once the gripper is on the button, we can push it.
    if check("the robot's gripper is touching the button"):
        robot.push("button")