# Steps:
    #  1. Line up the gripper vertically
    #  2. Move the gripper close to the wall
    #  3. Move the gripper forward to push the button
    # First, we need to line up the gripper vertically to make sure we hit the
    # button when we push.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button")
    # If there is a wall in the way, move the gripper close to the wall so that
    # we can push the button over the wall.
    if check("there is an obstacle between the robot and the button"):
        robot.move_gripper("close to the wall")
    # Now that the gripper is close to the wall, we can push the button by moving
    # the gripper forward.
    if check("the robot's gripper is near the button"):
        robot.move_gripper("in front of the button")