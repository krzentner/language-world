# Steps:
    #  0. Check if there is a wall in the way
    #  1. Put gripper roughly above the puck, on the side without the wall
    #  2. Drop gripper around the puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    # First, check if there is a wall in the way
    if check("there is a wall in the way"):
        # If there is a wall in the way, move the robot around the wall
        robot.move_around_wall()
    # Put the gripper above the puck on the side without the wall, so that we
    # don't bump into the wall while trying to grab the puck.
    if check("the robot's gripper is not above the puck on the side without the wall"):
        robot.move_gripper("above the puck on the side without the wall")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.move_gripper("near the target location on the side without the wall")