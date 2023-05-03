

1. Put gripper above puck  
2. Drop gripper around puck  
3. Line up gripper with the wall   
4. Move gripper below wall and pick up puck  
5. Move puck to goal  

# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
# def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Line up gripper with the wall
    #  4. Move gripper below wall and pick up puck
    #  5. Move puck to goal
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    # We need to get it close, but not too close - the wall should be in the
    # way.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # Now, we need to line up the gripper with the wall in order to trap the
    # puck between the wall and the gripper.
    # Move the gripper to a location that is close the wall, while still being
    # on the side of the puck.
    if check("the robot's gripper is not horizontally aligned with wall and the robot's gripper is not directly adjacent to the wall"):
        robot.move_gripper("directly adjacent to the wall")
    # Now move the gripper below the wall to trap the puck.
    if check("the robot's gripper is horizontally aligned with wall and the puck is not below the robot's gripper"):
        robot.move_gripper("below the wall", close_gripper=True)
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is below wall and the robot's gripper is closed"):
        robot.move_gripper("near the target location")