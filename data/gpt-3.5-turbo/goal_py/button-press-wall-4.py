# Steps:
    #  1. Put gripper near the wall, but below the button
    #  2. Tilt the gripper 90 degrees to be perpendicular to the wall
    #  3. Move the gripper forward to push the button
    # First, move the gripper near the wall and below the button.
    if check("the robot's gripper is not near the wall"):
        robot.move_gripper("near the wall and below the button")
    # Once the gripper is near the wall, tilt it 90 degrees to be perpendicular
    # to the wall.
    if check("the robot's gripper is not perpendicular to the wall"):
        robot.move_gripper("perpendicular to the wall")
    # Finally, move the gripper forward to push the button.
    if check("the robot's gripper is not touching the button"):
        robot.move_gripper("touching the button")