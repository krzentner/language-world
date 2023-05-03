
    # Steps:
    #  1. Put the gripper in front of the wall
    #  2. Push the wall down
    #  3. Line the gripper up with the button
    #  4. Push down on the button
    # 
    # First, put the gripper in front of the wall.
    if check("the robot's gripper is not in front of wall"):
        robot.move_gripper("in front of the wall")
    # Then, push the wall down so that the gripper can access the button.
    if check("the wall is not pushed down"):
        robot.move_gripper("downwards")
    # Line the gripper up with the button from behind the wall.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Finally, press the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button")