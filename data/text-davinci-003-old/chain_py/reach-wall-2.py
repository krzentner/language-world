
    # Steps:
    #  1. Reach towards the wall
    #  2. Push the gripper against the wall
    #  3. Reach towards the target with the wall obstructing the approach
    # To reach the target, we need to get past the wall.
    # First, reach towards the wall itself.
    if check("the wall is not near the robot's gripper"):
        robot.reach("wall")
    # Once the wall is close, push the robot's gripper against the wall.
    if check("the wall is near the robot's gripper"):
        robot.push("gripper against wall")
    # Now that the robot's gripper is past the wall, reach for the target with
    # the wall obstructing the approach.
    if check("the target is not near the robot's gripper and the wall is past the robot's gripper"):
        robot.reach("to target")