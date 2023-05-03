# reach-wall: reach to the target location with a short wall in the way
# def reach_wall(robot):
    # Steps:
    #  1. Check if gripper is blocked by wall
    #  2. Move gripper above target if blocked
    #  3. Move gripper towards target
    #  4. Check if gripper is blocked by wall
    #  5. Move gripper above target
    #  6. Move gripper towards target
    # We need to check if the gripper is blocked by the wall. If it is, move the
    # gripper above the target and attempt to reach for it again.
    if check("the robot's gripper is blocked by wall"):
        robot.move_gripper("above the reach target")
    if check("the robot's gripper is not near the reach target"):
        robot.move_gripper("near the reach target")
    # If the gripper is now blocked by the wall again, move it above the target
    # and then towards the target.
    if check("the robot's gripper is blocked by wall"):
        robot.move_gripper("above the reach target")
    if check("the robot's gripper is not near the reach target"):
        robot.move_gripper("near the reach target")