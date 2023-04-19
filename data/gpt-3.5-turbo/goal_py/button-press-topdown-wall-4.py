# Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Move the robot to the side of the wall
    #  3. Move the robot over the top of the button
    #  4. Push down on the button from the top
    # First, put the gripper in line with the button from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Move the robot to the side of the wall so that it can reach the button.
    if check("the robot is not next to the wall"):
        robot.move("next to the wall")
    # Move the robot over the top of the button.
    if check("the robot is not over the top of the button"):
        robot.move("over the button")
    # Push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button")