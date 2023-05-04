
    # Steps:
    #  1. Reach towards the target
    #  2. If the robot's gripper is to the left of the wall, move it to the right of the wall
    #  3. If the robot's gripper is to the right of the wall, move it to the left of the wall
    # We don't have any objects to manipulate, so we can just move the robot's
    # gripper directly to the target location
    if check("the robot's gripper is not near reach target"):
        robot.move_gripper("near the reach target", allow_partial=True)
    # Make sure we are left of the wall.
    if check("the robot's gripper is left of the wall"):
        robot.move_gripper("right of the wall")
    # Now we are in the right spot to reach.
    if check("the robot's gripper is right of the wall"):
        robot.move_gripper("above the reach target")

# push-wall: push the puck to the target location with a short wall in the way
def push_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. If the robot's gripper is to the left of the wall, move it to the right of the wall
    #  4. If the robot's gripper is to the right of the wall, move it to the left of the wall
    #  5. Slide puck to goal
    # If the puck is not below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck"):
        robot.move_gripper("above the puck")
    # If the gripper is above the puck but not near it, move the gripper down
    # to the puck to slide it.
    if check("the robot's gripper is not near puck"):
        robot.move_gripper("above the puck", close_gripper=True)
    # Check if we're on the wrong side of the wall.
    if check("the robot's gripper is left of the wall"):
        robot.move_gripper("right of the wall")
    # Now we are in the