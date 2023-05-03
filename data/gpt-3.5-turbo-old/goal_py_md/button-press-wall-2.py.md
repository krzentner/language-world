# button-press-wall: push the button from the front with a short wall in the way
# def button_press_wall(robot):
    # Steps:
    #  1. Find a clear path to button
    #  2. Move the robot to the side of the wall
    #  3. Move the robot towards the button until robot is closer to it than the wall
    #  4. Line up the gripper with the button
    #  5. Push down on the button
    # First, use the robot's sensors to detect any obstacles blocking the path to
    # the button.
    if check("there is an obstacle in the way"):
        # If there is an obstacle, try to find a clear path to the button.
        if check("there is no clear path to the button"):
            # If there is no clear path to the button, move the robot around the
            # obstacle to find a clear path.
            robot.move_to("right of the obstacle")
            robot.move_to("in front of the obstacle")
            robot.move_to("left of the obstacle")
        else:
            # If there is a clear path to the button, move the robot towards the
            # button until it is closer to it than the obstacle.
            robot.move_to("in front of the button")
    # Once the robot is in front of the button and the gripper is above it,
    # push down on the button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button")