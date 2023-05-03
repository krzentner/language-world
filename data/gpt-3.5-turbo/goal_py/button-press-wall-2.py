# Steps:
    #  1. Line up the gripper to be on one side of the wall
    #  2. Position gripper over the button, while avoiding the wall
    #  3. Push the button
    # First, position the gripper on one side of the wall.
    if check("the robot's gripper is not vertically aligned with the wall"):
        robot.move_gripper("vertically aligned with the wall")
    # Once the gripper is on the side of the wall, position it over the button.
    # Since there is a wall in the way, we need to move the gripper to the side
    # in order to avoid it.
    if check("the robot's gripper is on one side of the wall and the robot's gripper is not almost vertically aligned with the button"):
        robot.move_gripper("almost vertically aligned with the button", close_gripper=True)
    # Once the gripper is lined up with the button, push it.
    if check("the robot's gripper is almost vertically aligned with the button"):
        robot.move_gripper("near the button")