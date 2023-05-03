# push-wall: slide the puck to the target location with a small wall in the way
def push_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to wall
    #  4. Move gripper to front of wall
    #  5. Push gripper against wall
    #  6. Move gripper to top of puck
    #  7. Slide puck to goal
    # The robot needs to push the puck against a small wall before sliding it to the
    # target location.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.move_gripper("above the puck", close_gripper=True)
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it towards the wall.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.move_gripper("near the wall")
    # If the gripper is near the wall, push against it.
    if check("the robot's gripper is against the wall"):
        robot.move_gripper("near the puck")
    # Move to the target location and release the puck.
    if check("the robot's gripper is near the target location"):
        robot.move_gripper("above the target location", close_gripper=False)