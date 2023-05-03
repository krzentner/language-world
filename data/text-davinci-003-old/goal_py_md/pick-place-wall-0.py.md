

# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
# def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Move gripper around the wall
    #  3. Drop gripper around the puck
    #  4. Close gripper around the puck
    #  5. Move the puck to goal
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not around wall"):
        robot.move_gripper("above the puck")
    # Move the gripper around the wall.
    if check("the robot's gripper is not around wall"):
        robot.move_gripper("around the wall")
    # If the gripper is around the wall, grab the puck.
    if check("the robot's gripper is around wall and the robot's gripper is not around puck"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is around the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is around the puck and the robot's gripper is closed"):
        robot.move_gripper("near the target location")