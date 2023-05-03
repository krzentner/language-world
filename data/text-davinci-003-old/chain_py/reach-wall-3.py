
    # Steps:
    #  1. Reach towards the target
    #  2. Move robot's arm to the side to clear the wall
    # We can just move the robot's gripper directly to the target location
    if check("robot's gripper is not near target"):
        robot.reach("to goal")
    # If the wall is still in the way, we need to move the arm to the side to
    # clear it.
    # This is done by subtracting a certain value from the x coordinate of the
    # target location. Move the arm until it crosses the wall.
    if check("the wall is still in the way and the robot's gripper is not near target"):
        robot.move("the arm to the side")