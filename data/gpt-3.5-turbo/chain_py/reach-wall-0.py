# Steps:
    #  1. Move gripper to just in front of the wall
    #  2. Slide gripper over the wall
    #  3. Move gripper to goal location
    # First, move the gripper just in front of the wall.
    if check("the robot's gripper is not just in front of the wall"):
        robot.move("gripper to just in front of the wall")
    # Once the gripper is in position, slide it over the wall.
    if check("the robot's gripper is just in front of the wall"):
        robot.slide("gripper over the wall")
    # Once the gripper is over the wall, move it to the goal location.
    if check("the robot's gripper is over the wall and not at the goal location"):
        robot.move("gripper to goal location")