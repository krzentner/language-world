# Steps:
    #  1. Move gripper to just above the wall
    #  2. Move gripper over the wall to the target
    # To reach the target with a wall in the way, we need to move the gripper
    # above the wall and then over it.
    # First, move the gripper above the wall.
    if check("the robot's gripper is not above the wall"):
        robot.move("gripper above wall")
    # Once the gripper is above the wall, move it over the wall to the target.
    if check("the robot's gripper is above the wall and not at the target location"):
        robot.slide("gripper over wall to reach target")