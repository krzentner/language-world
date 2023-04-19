# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
# def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    #  5. Place puck at target location while navigating around the wall
    # First, put the gripper roughly above the puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.move_gripper("near the target location with the wall in the way")
    # If the gripper is near the target location but can't reach it because of the wall, we need to navigate around the wall.
    if check("the robot's gripper is near the target location with the wall in the way"):
        robot.move_gripper("above the wall", close_gripper=True)
        robot.move_gripper("near the target location")
    # Once we're above the target location, we can release the puck.
    if check("the robot's gripper is above the target location"):
        robot.move_gripper("above the target location", close_gripper=False)