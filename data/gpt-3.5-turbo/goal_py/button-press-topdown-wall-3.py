# Steps:
    #  1. Put gripper above button and wall
    #  2. Move gripper forward to touch the wall
    #  3. Move gripper down to push button
    # Because there is a wall in the way, we need to carefully position the
    # gripper to avoid hitting the wall. First, put the gripper above the button
    # and wall.
    if check("the robot's gripper is not above the button and wall"):
        robot.move_gripper("above the button and the wall")
    # If the gripper is not touching the wall, move it forward until it touches.
    # Because we don't know how far away the wall is, we need to move the gripper
    # forward very slowly and check frequently.
    if check("the robot's gripper is not touching the wall and the robot's gripper is not near the button"):
        robot.move_gripper("almost touching the wall")
    # Once the gripper is touching the wall, push down on the button by moving
    # the gripper down.
    if check("the robot's gripper is touching the wall"):
        robot.move_gripper("near the button")