# Steps:
    #  1. Put gripper above puck to the side of the wall
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal
    # First, put the gripper to the side of the wall and above the puck, so that
    # we're not bumping into the wall while trying to slide the puck.
    if check("the robot's gripper is not to the side of the wall and above the puck"):
        robot.move_gripper("to the side of the wall and above the puck")
    # If the gripper is above the puck but not near it, move the gripper down to
    # the puck to slide it.
    if check("the robot's gripper is above the puck and the puck is not below the robot's gripper"):
        robot.move_gripper("above the puck", close_gripper=True)
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.move_gripper("above the target location")