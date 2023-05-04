
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to edge of wall
    #  4. Close the gripper to lift up the puck
    #  5. Slide the puck to the target location
    # The robot can slide the puck by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    # Because the wall is in the way, we only push the puck to the edge of the
    # wall.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.move_gripper("above the puck", close_gripper=True)
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the edge of the wall.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.move_gripper("above the puck")
    # When the gripper is near the puck but not above it, we've probably pushed
    # the puck against the edge of the wall and should lift up the puck.
    # Closing the gripper is probably enough.
    if check("the robot's gripper is near the puck and the puck is not below the robot's gripper"):
        robot.move_gripper("near the target location")

# pick-wall: pick up the puck with a small wall in the way
def pick_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  