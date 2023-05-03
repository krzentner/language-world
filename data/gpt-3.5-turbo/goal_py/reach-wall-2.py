# Steps:
    #  1. Move gripper over the wall
    #  2. Lower gripper to target location
    # We'll need to move the gripper over the wall using an arc-like motion.
    if check("the robot's gripper is not over the wall"):
        robot.move_gripper("over the wall")
    # Once the gripper is over the wall, we can lower it directly to the target
    # location.
    if check("the robot's gripper is over the wall"):
        robot.move_gripper("near the reach target")