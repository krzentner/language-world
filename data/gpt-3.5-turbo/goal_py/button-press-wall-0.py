# Steps:
    #  1. Move the gripper near the button
    #  2. Close the gripper around the button
    #  3. Push the button from the front while avoiding the wall
    # To press the button, we need to approach it from the front while avoiding
    # the short wall in the way.
    # If the robot's gripper is not near the button, move it to the button.
    if check("the robot's gripper is not near the button"):
        robot.move_gripper("near the button", close_gripper=True)
    # Now that the gripper is close to the button, we need to carefully move it
    # forward while avoiding the wall.
    # First, move the gripper forward until it touches the wall.
    if check("the robot's gripper is not in contact with the wall and the button"):
        robot.move_gripper("forward", tolerance=0.1)
    # If the wall is in the way but the gripper could move around it, move the
    # gripper around the wall.
    # Since we're just pushing a button, we don't need to be too careful about
    # the direction we're pushing in, so we can just move the gripper around the
    # wall if we can.
    if check("the robot's gripper is in contact with the wall but the gripper could move around the wall"):
        robot.move_gripper("left of the wall")
    # Once the gripper is left of the wall, we can move it forward again to push
    # the button.
    if check("the robot's gripper is left of the wall and in contact with the button"):
        robot.move_gripper("forward")