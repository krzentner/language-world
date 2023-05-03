# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
# def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Lift puck up and over the wall
    #  5. Move puck to target location
    # If the wall is in the way of the robot's gripper, we need to first move the
    # gripper to the side of the wall.
    if check("the wall is between the robot's gripper and the puck"):
        robot.move_gripper("left of the wall")
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.move_gripper("above the wall")
    # If we can lift the puck over the wall, move it directly to the target location.
    if check("the robot's gripper is above the wall and the puck can be lifted over it"):
        robot.move_gripper("above the target location")
    # If we cannot lift the puck over the wall, move the gripper to the other side
    # of the wall so that it can grab the puck from there.
    if check("the robot's gripper is above the wall and the puck cannot be lifted over it"):
        robot.move_gripper("right of the wall")
        robot.move_gripper("vertically aligned with the puck")
        robot.move_gripper("near the puck", close_gripper=True)
        robot.move_gripper("above the wall")
        robot.move_gripper("above the target location")