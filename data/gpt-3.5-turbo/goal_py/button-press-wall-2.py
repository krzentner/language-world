# Steps:
    #  1. Put gripper to the right of the wall
    #  2. Move the gripper over the wall
    #  3. Push the button
    # If the gripper is not to the right of the wall, move it to the right of
    # the wall to start.
    if check("the robot's gripper is not right of the wall"):
        robot.move_gripper("right of the wall")
    # Once the gripper is to the right of the wall, move it over the wall to
    # the button.
    if check("the robot's gripper is right of the wall and the robot's gripper is not near the button"):
        robot.move_gripper("above the button", close_gripper=True)