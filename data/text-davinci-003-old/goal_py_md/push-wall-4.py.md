

Steps:
1. Put gripper above puck
2. Push gripper into top of puck
3. Slide puck to the small wall
4. Push the puck out of the small wall towards the goal

# push-wall: slide the puck to the target location with a small wall in the way
# def push_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to the small wall
    #  4. Push the puck out of the small wall towards the goal
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
        robot.move_gripper("near the small wall")
    # If the puck is near the small wall, push the puck out of the wall towards
    # the goal.
    if check("the puck is near the small wall"):
        robot.move_gripper("near the target location")