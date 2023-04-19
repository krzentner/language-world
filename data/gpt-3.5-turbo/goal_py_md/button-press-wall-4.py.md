# button-press-wall: push the button from the front with a short wall in the way
# def button_press_wall(robot):
    # Steps:
    #  1. Move gripper to the side of the wall
    #  2. Position gripper above the button
    #  3. Move gripper forward to press the button
    # First, move the gripper to the side of the wall that is blocking the robot's path to the button
    if check("the robot's gripper is not beside the wall"):
        robot.move_gripper("beside the wall")
    # Once the gripper is beside the wall, position it above the button
    if check("the robot's gripper is not above the button"):
        robot.move_gripper("above the button")
    # Move the gripper forward to press the button
    if check("the robot's gripper is not near the button"):
        robot.move_gripper("near the button")