
    # Steps:
    #  1. Reach towards the target
    #  2. Reach around the wall
    #  3. Reach to the target
    # We don't have any objects to manipulate, so we can just move the robot's
    # gripper directly to the target location
    if check("the robot's gripper is not near reach target"):
        robot.reach("to goal")
    # If the wall is in the way, move the gripper to the side of the wall and
    # then towards the target.
    if check("the wall is in the way of robot's gripper"):
        robot.reach("around wall")
    # If the gripper is still not close to the target, move the gripper towards
    # the target.
    if check("the robot's gripper is not near target"):
        robot.reach("to goal")