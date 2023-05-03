# button-press-wall: push the button from the front with a short wall in the way
# def button_press_wall(robot):
    # Steps:
    #  1. Line up the gripper with the button from the front
    #  2. Move the gripper forward until it hits the wall
    #  3. Push against the wall to compress the gripper and press the button
    # To press a button with a short wall in the way, first line up the robot's
    # gripper with the button from the front.
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Next, move the gripper forward until it hits the wall.
    if check("the robot's gripper is not against the wall"):
        robot.move_gripper("against the wall")
    # Once the gripper is against the wall, push against the wall to compress
    # the gripper and press the button.
    if check("the robot's gripper is against the wall"):
        robot.move_gripper("into the wall")