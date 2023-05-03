

The goal of this task is to push the button from the front, with a short wall in the way.

# button-press-wall: push the button from the front with a short wall in the way
def button_press_wall(robot):
    # Steps:
    #  1. Align the gripper with the button as viewed from the front
    #  2. Push the button in between the wall and the button
    #  3. Push the button to activate it
    # First, align the gripper with the button as viewed from the front.
    if check("the robot's gripper is not aligned with the button from the front"):
        robot.put("gripper aligned with button from the front")
    # Once the gripper is aligned with the button from the front, we should be 
    # able to push the button in between the wall and the button.
    if check("the robot's gripper is aligned with the button from the front and the button is not in between wall and button"):
        robot.push("button in between wall and button")
    # If the button is in between the wall and the button, push the button to 
    # activate it.
    if check("the button is in between wall and button"):
        robot.push("button to activate it")