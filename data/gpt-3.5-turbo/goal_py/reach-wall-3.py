# Steps:
    #  1. Put the gripper above the wall
    #  2. Move the gripper over the wall
    #  3. Put the gripper down to reach the target
    # To reach the target when there's a wall in the way, we need to move the
    # gripper over the wall.

    # First, move the gripper roughly above the wall.
    if check("the robot's gripper is not above the wall"):
        robot.move_gripper("above the wall")
    # Once the gripper is above the wall, we should be able to move it over the
    # wall.
    if check("the robot's gripper is above the wall and the robot's gripper is not over the target"):
        robot.move_gripper("over the wall")
    # Once the gripper is over the wall, we can simply move it down to reach the
    # target.
    if check("the robot's gripper is over the target"):
        robot.move_gripper("near the reach target")