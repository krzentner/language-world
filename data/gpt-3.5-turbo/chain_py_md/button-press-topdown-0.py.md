# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Put gripper above the button
    #  2. Push gripper down onto the button
    #  3. Move the gripper slightly to activate the button
    # First, put the gripper above the button.
    if check("the robot's gripper is not above the button"):
        robot.put("gripper above button")
    # If the gripper is not pushing down on the button, push it down.
    if check("the robot's gripper is above the button and the robot's gripper is not pushing down on the button"):
        robot.push("gripper down onto button")
    # If the gripper is now pushing down on the button, move it slightly to activate the button.
    if check("the robot's gripper is pushing down on the button"):
        robot.move("gripper slightly to activate button")