
    # Steps:
    #  1. Put gripper near puck above wall
    #  2. Push puck on top of wall
    #  3. Push puck to goal
    #
    # The robot can't easily slide the puck if the wall is in the way, so instead
    # we have to lift the puck over the wall, then slide it.
    # Put the gripper close to the puck, but above the wall.
    if check("the robot's gripper is not above wall and the robot's gripper is not near the puck"):
        robot.move_gripper("above the wall")
    # If the gripper is near the puck and above the wall, push the puck onto the
    # wall.
    if check("the robot's gripper is above the wall and the puck is not on the wall"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the puck is on the wall, we can slide the puck to the target location.
    if check("the puck is on the wall"):
        robot.move_gripper("near the target location")