
    # Steps:
    #  1. Line up the gripper as viewed from the side
    #  2. Push against the wall
    #  3. Pull the wall away from the button
    # First line the gripper with the wall.
    if check("the robot's gripper is not vertically aligned with wall"):
        robot.move_gripper("vertically aligned with the wall")
    # Push it until the wall is near the button.
    if check("the wall is near the button"):
        robot.move_gripper("in the gap between the wall and the button")
    # Pull the wall away from the button.
    if check("the robot's gripper is in the gap between the wall and the button"):
        robot.move_gripper("around the button")