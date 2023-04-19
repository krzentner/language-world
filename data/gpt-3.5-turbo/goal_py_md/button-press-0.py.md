# button-press: push the button from the front
# def button_press(robot):
    # Steps:
    #  1. Line up the robot's gripper with the button from the front
    #  2. Push the button
    if check("the robot's gripper is not aligned with the button from the front"):
        robot.move_gripper("aligned with the button from the front", close_gripper=True)
    # Once the gripper is aligned with the button from the front, push the button
    if check("the robot's gripper is aligned with the button from the front"):
        robot.move_gripper("near the button")