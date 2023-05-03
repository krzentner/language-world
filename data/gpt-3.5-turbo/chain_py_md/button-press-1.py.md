# button-press: push the button from the front
def button_press(robot):
    # Steps:
    #  1. Put gripper in front of button
    #  2. Move gripper down to button
    #  3. Push button
    # We need to put the gripper in front of the button before we can interact with it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not in front of the button"):
        robot.put("gripper in front of button")
    # Once the gripper is in front of the button, we can move it down to the button to push it.
    if check("the robot's gripper is in front of the button and the robot's gripper is not touching the button"):
        robot.move("gripper down to button")
    # Once the gripper is touching the button, we can push it.
    if check("the robot's gripper is touching the button"):
        robot.push("button forward")