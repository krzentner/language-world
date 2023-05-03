
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper onto top of puck
    #  3. Slide puck to goal, avoiding the wall
    #  4. Slide puck past the wall
    # We still need to trap the puck with the robot's gripper from above, but
    # we also need to make sure that the robot avoids the wall while doing this.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("horizontally away from the wall")
    # If the gripper needs to be further away from the wall, move the gripper
    # sideways in the opposite direction of the wall.
    if check("the robot's gripper is horizontally away from the wall and the puck is not below the robot's gripper as seen from overhead"):
        robot.move_gripper("vertically aligned with the puck", close_gripper=True)
    # If the robot's gripper is near the puck and the puck is below the robot's
    # gripper as seen from above, we've probably trapped the puck and can slide
    # it to the target location, as long as the wall isn't too close.
    if check("the robot is far away from wall and the robot's gripper is near the puck and the puck is below the robot's gripper as seen from overhead"):
        robot.move_gripper("above the target location")