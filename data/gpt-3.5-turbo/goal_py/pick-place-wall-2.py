# Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck while avoiding the wall
    #  3. Close gripper around puck
    #  4. Move puck to goal while avoiding the wall
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck while avoiding
    # the wall.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", avoid=["wall"], close_gripper=True)
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.move_gripper("near the target location", avoid=["wall"])