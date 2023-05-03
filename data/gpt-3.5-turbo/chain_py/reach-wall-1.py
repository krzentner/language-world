# Steps:
    #  1. Move gripper as close as possible to wall without touching it
    #  2. Move gripper to reach target
    #  3. Adjust position as necessary to reach target without hitting wall
    # To reach the target with a wall in the way, we first need to get as close
    # as possible to the wall without bumping it.
    if check("the robot's gripper is not close to the wall"):
        robot.move("gripper to near wall")
    # Once we're close to the wall, we can move the gripper towards the reach
    # target.
    if check("the robot's gripper is close to the wall"):
        robot.move("gripper to reach target")
    # If the gripper is about to bump the wall, we need to adjust its position.
    if check("the robot's gripper is going to hit the wall"):
        robot.adjust("gripper position to avoid wall")