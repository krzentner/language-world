
    # Steps:
    #  1. Reach towards the target
    #  2. Move around the wall
    # We don't have any objects to manipulate, so we can just move the robot's
    # gripper directly to the target location.
    if check("the robot's gripper is not near reach target and the short wall is not in the way"):
        robot.reach("to goal")
    # If the wall is in the way, we might have a bit of trouble reaching the
    # target.
    # Moving the gripper above the wall and then sliding it gently to the goal
    # might work.
    if check("the robot's gripper is not near reach target and the short wall is in the way"):
        robot.put("gripper above wall")
        robot.slide("gripper to goal")