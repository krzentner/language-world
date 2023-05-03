
    # Steps:
    #  1. Reach around the wall
    # We can't reach directly to the target location because of the wall, but we
    # can reach past the wall and move the gripper the rest of the way.
    if check("the robot's gripper is not past the wall"):
        robot.reach("around wall")
    # If the gripper is to the left side of the wall, move it past the wall.
    if check("the wall is between the robot's gripper and the reach target"):
        robot.reach("past wall")
    # Once the gripper is past the wall, just move it to the target location.
    if check("the wall is left of the robot's gripper"):
        robot.reach("to target")