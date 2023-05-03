# Steps:
    #  1. Put gripper above the puck
    #  2. Drop gripper around the puck
    #  3. Close gripper around the puck
    #  4. Move the puck over the wall
    #  5. Move the puck to the goal
    # We'll need to move the puck over the wall before we can bring it to the goal.
    # First, put the gripper roughly above the puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck and closed, we can try to lift the puck over
    # the wall.
    if check("the robot's gripper is near the puck and closed"):
        robot.move_gripper("above the wall")
    # Once the gripper is over the wall, move the gripper to the goal.
    if check("the robot's gripper is above the wall and near the target location"):
        robot.move_gripper("near the target location")