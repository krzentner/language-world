
    # Steps:
    #  1. Reach towards the wall
    #  2. Reach around the wall
    #  3. Reach towards the target
    # The robot can reach the target without having to manipulate any objects,
    # but it must first reach the wall, then around it.
    # Start by moving the gripper near the wall.
    if check("the robot's gripper is not near wall"):
        robot.move_gripper("near the wall")
    # Move around the wall, so that the gripper is on the other side of it.
    if check("the robot's gripper is not around wall"):
        robot.move_gripper("around the wall")
    # Now that the gripper is in the same side as the target, move it near the
    # target.
    if check("the robot's gripper is not near target"):
        robot.move_gripper("near the target")