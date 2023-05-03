
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    #  5. Spin the puck by rotating the robot's wrist
    #  6. Drop the puck onto the goal slide
    #  7. Spin the puck again
    # The first few steps are the same as a regular pick-place.
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck and open, maybe we can grab it by
    # closing the gripper.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.move_gripper("near the target location")
    # The wall should be at the target location, so that the robot will have to
    # spin the puck around the wall in order to get it over the wall and onto the
    # goal slide.
    # First, rotate the robot's wrist to the side to spin the puck around the wall.
    if check("the robot's wrist is not turned towards the wall"):
        robot.rotate_wrist("towards the wall")
    # Now that the puck is rotated, lower the puck to the goal slide.
    if check("the robot's gripper is not vertically aligned with the goal slide"):
        robot.move_gripper("vertically aligned with the goal slide")
    # Finally, rotate the robot's wrist again to spin the puck around the wall
    # the other way.
    if check("the robot's wrist is not turned away from the wall"):
        robot.rotate_wrist("away from the wall")