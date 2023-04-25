
    # Steps:
    #  1. Put gripper in front of the wall
    #  2. Push against the wall
    #  3. Move the gripper to the button
    #  4. Push the button
    # If the gripper isn't in front of the wall, move it there.
    if check("the robot's gripper is not in front of the wall"):
        robot.move_gripper("in front of the wall")
    # If the gripper is in front of the wall, push against it.
    if check("the robot's gripper is in front of the wall"):
        robot.move_gripper("forward aligned with the wall")
    # If the gripper is in front of the wall and not near the button, move it
    # near the button.
    if check("the robot's gripper is not near the button"):
        robot.move_gripper("near the button")
    # Once the gripper is near the button, push it.
    if check("the robot's gripper is near the button"):
        robot.move_gripper("forward aligned with the button")