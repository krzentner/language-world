
    # Steps:
    #  1. Put gripper above puck
    #  2. Push against the wall, the puck should move
    # First, move the robot's gripper to be above the puck
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # Push against the wall
    if check("the robot's gripper is above the puck and the puck is in front of a wall"):
        robot.move_gripper("horizontally aligned with the wall")
    # If the puck is moving, we can push it to the target location.
    if check("puck is almost horizontally aligned with the wall and the target is not left of puck"):
        robot.move_gripper("above target location")