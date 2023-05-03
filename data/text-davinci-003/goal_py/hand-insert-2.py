
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to the goal
    #  5. Put gripper back to starting position
    # First, put the gripper above the puck so that it can grab it without
    # bumping it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # Once the gripper is closed around the puck, move the puck to the target
    # location.
    if check("the robot's gripper is closed"):
        robot.move_gripper("near the target location")
    # Once the puck is at the target location, open the gripper and move back
    # to the starting position.
    if check("the robot's gripper is above the target location"):
        robot.move_gripper("above the puck", open_gripper=True)