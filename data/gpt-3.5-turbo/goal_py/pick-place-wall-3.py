# Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Lift puck over the wall
    #  5. Move puck to goal
    # This task is similar to pick-place, but with a wall in the way.
    # First, put the gripper roughly above the puck so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck and closed, lift the puck over the wall by
    # moving the gripper up.
    if check("the robot's gripper is around puck"):
        robot.move_gripper("above the wall")
    # Once the gripper is over the wall, move the gripper towards the target
    # location to place the puck.
    if check("the robot's gripper is near the target location"):
        robot.move_gripper("near the target location")