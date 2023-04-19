
    # Steps:
    #  1. Reach towards the target
    #  2. Move around the wall
    # We need to move around the wall if the robotic arm can't reach the target
    # location directly.
    if check("the robot's gripper is not near target location"):
        robot.move_gripper("near the target location")
    # To move around the wall, we can use the gripper to push against the wall
    # and move it's way around.
    # Move the gripper up the wall until the end of the wall is reached.
    if check("the robot's gripper is not near the wall"):
        robot.move_gripper("to the wall")
    # Once the end of the wall is reached move the gripper to the other side of
    # the wall.
    if check("the robot's gripper is near the wall"):
        robot.move_gripper("around the wall")
    #Continue this process until the target location is reached.
    if check("the robot's gripper is not near target location"):
        robot.move_gripper("near the target location")