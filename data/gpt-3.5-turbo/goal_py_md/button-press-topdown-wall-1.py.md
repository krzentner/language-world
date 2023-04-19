# button-press-topdown-wall: push the button down from above with a short wall in the way
# def button_press_topdown_wall(robot):
    # Steps:
    # 1. Line up the gripper with the button
    # 2. Move the robot's base to the side
    # 3. Move the gripper down to press the button
    # To press the button from above with a wall in the way, we need to move the robot's
    # base out of the way to the side.
    if check("the robot's base is not aligned with the side of the wall"):
        robot.move_base("aligned with the side of the wall")
    # Once the robot's base is out of the way, we can line up the gripper with the button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Now we can move the gripper down to press the button.
    if check("the robot's gripper is not touching the button"):
        robot.move_gripper("on the button")