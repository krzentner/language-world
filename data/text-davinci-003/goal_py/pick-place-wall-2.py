
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around the puck
    #  3. Close gripper around the puck
    #  4. Move the puck above the wall
    #  5. Move the puck to the target location
    # First, put the gripper above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck, move it up until it is above the wall.
    if check("the robot's gripper is above the puck and the puck is not above the wall"):
        robot.move_gripper("above the wall")
    # Once the puck is above the wall, move it to the target location (with the
    # gripper).
    if check("the puck is above the wall and put the robot's gripper is not near the target location"):
        robot.move_gripper("near the target location")