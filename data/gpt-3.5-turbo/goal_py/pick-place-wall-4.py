# Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Lift puck above wall
    #  5. Move puck to goal while keeping it above wall
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        # If the puck is on the right side of the wall, move the gripper to the
        # left of the wall.
        if check("the puck is right of the wall"):
            robot.move_gripper("left of the wall")
            # Once the gripper is to the left of the wall, lift the puck above the
            # wall.
            if check("the robot's gripper is left of the wall and the robot's gripper is not above the wall"):
                robot.move_gripper("above the wall")
            # Once the puck is above the wall, move it to the goal while also keeping
            # it above the wall.
            if check("the robot's gripper is above the wall and the robot's gripper is not above the target location"):
                robot.move_gripper("above the target location", keep_above="wall")
        # Otherwise, the puck is on the left side of the wall, so just move it to
        # the goal location.
        else:
            robot.move_gripper("near the target location")