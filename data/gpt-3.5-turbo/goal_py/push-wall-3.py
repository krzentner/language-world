# Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Move the puck around the wall to the target location
    # The robot can't slide the puck directly to the target location because a wall is in the way.
    # If the puck isn't below the gripper as seen from above, move the gripper above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.move_gripper("above the puck", close_gripper=True)
    # If the gripper is near the puck, we've probably trapped the puck and need to move it around the wall.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        # Move the gripper to the right of the wall
        robot.move_gripper("right of the wall")
        # Move the puck down to the wall level
        robot.move_gripper("at the level of the wall")
        # Move the gripper to the left of the wall towards the target location
        robot.move_gripper("left of the wall towards the target location")