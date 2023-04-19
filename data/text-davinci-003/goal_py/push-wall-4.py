
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into wall
    #  3. Move gripper around wall into puck
    #  4. Slide puck to goal
    # Start by putting the gripper above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the wall is above the puck, push down onto the wall first.
    if check("the wall is below the robot's gripper"):
        robot.move_gripper("into the wall")
    # Now that the gripper is pressing down on the wall, it should be possible
    # to move it around the wall and into the puck.
    if check("the robot's gripper is against the wall and the robot's gripper is not near the puck"):
        robot.move_gripper("near the puck")
    # If the gripper is over the puck, close the gripper to trap the puck.
    if check("the robot's gripper is near the puck"):
        robot.move_gripper("below the wall", close_gripper=True)
    # If the gripper is holding onto the puck, slide it around the wall and to
    # the target location.
    if check("the puck is below the robot's gripper and the gripper is closed"):
        robot.move_gripper("above the target location")