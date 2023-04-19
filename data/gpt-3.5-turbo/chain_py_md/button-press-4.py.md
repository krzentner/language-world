# button-press: push the button from the front
def button_press(robot):
    # Steps:
    # 1. Align the gripper with the button from the front
    # 2. Push the button
    # We need to align the gripper with the button from the front by moving the
    # robot's arm sideways.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.move("gripper to front of button")
    # Once the gripper is aligned with the button, push down on the button.
    if check("the robot's gripper is horizontally aligned with button"):
        robot.push("down on button")