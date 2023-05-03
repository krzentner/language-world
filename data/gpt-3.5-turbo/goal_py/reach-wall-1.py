# Steps:
    #  1. Move gripper above the wall
    #  2. Move gripper around the wall
    #  3. Move gripper to target
    # We can't just move the gripper directly to the target location because
    # there's a wall in the way. So first we need to move the gripper above the
    # wall.
    if check("the robot's gripper is not above the wall"):
        robot.move_gripper("above the wall")
    # Once we're above the wall, we can move the gripper around it.
    if check("the robot's gripper is above the wall and not around the wall"):
        robot.move_gripper("around the wall")
    # Finally, we can move the gripper to the target location.
    if check("the robot's gripper is around the wall and not near the target"):
        robot.move_gripper("near the target location")