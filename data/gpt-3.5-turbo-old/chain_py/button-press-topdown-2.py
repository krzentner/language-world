Oops, it looks like there was a duplicate of a function above. Here's a new function:

# button-press-side: push the button in from the side
# def button_press_side(robot):
    # Steps:
    # 1. Put gripper next to the button
    # 2. Push gripper into the button to press it
    # First, put the gripper next to the button.
    if check("the robot's gripper is not next to the button"):
        robot.move("gripper next to button")
    # Once the gripper is next to the button, push it in to press the button.
    if check("the robot's gripper is next to the button"):
        robot.push("button in")