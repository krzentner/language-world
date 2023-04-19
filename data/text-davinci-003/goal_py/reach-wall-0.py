
    # Steps:
    #  1. Determine the shape of the wall
    #  2. If the wall is concave, and the robot's gripper is not against the wall, move the robot's gripper along the wall until it is
    #  3. If the wall is convex, and the robot's gripper is not against the wall, move robot's gripper up, then move along the wall until it is
    # We need to determine the shape of the wall first.
    # If the wall is concave, and the robot's gripper is not against the wall, move the gripper along the wall until it is.
    if check("the wall is concave and the robot's gripper is not against the wall"):
        robot.move_gripper("along the wall")
    # If the wall is convex, and the robot's gripper is not against the wall, move the gripper up, then move along the wall until it is.
    if check("the wall is convex and the robot's gripper is not against the wall"):
        robot.move_gripper("up and then along the wall")
    # Once the gripper is against the wall, move it to the target location.
    if check("the robot's gripper is against the wall"):
        robot.move_gripper("near the target location")