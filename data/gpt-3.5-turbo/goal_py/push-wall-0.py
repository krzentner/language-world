# Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal, avoiding the wall
    # Same approach as "push", but we need to make sure the gripper avoids the
    # wall. We can do this by moving the gripper to a position where the wall is
    # not blocking the path, and pushing the puck in that direction.
    # Move the gripper near the wall to start the push.
    if check("the robot's gripper is not near the wall"):
        robot.move_gripper("near the wall")
    # Move the gripper down onto the puck if it isn't already there.
    if check("the robot's gripper is not above puck"):
        robot.move_gripper("above the puck")
    # Find a direction to push the puck in. If the puck isn't currently blocked
    # by the wall, just push it straight to the goal. Otherwise, try to find
    # a direction towards the goal that doesn't hit the wall. We can do this by
    # finding the vector from the puck to the goal, and then rotating that vector
    # until it's not pointing at the wall.
    if check("the robot's gripper is above the puck"):
        puck_pos = robot.get_object_position("puck")
        goal_pos = robot.get_goal_position()
        wall_pos = robot.get_wall_position()

        goal_vec = goal_pos - puck_pos
        wall_vec = wall_pos - puck_pos

        # Rotate the goal vector away from the wall until it's no longer
        # pointing at it.
        while goal_vec.dot(wall_vec) > 0:
            goal_vec = goal_vec.rotate(np.pi / 4)
        target_pos = puck_pos + goal_vec

        robot.move_gripper("above the target position")