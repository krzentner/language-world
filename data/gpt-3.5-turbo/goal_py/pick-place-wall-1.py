# Steps:
    #  1. Put gripper above the puck
    #  2. Move to the side of the wall
    #  3. Move gripper above the puck and around the wall
    #  4. Close gripper around puck
    #  5. Move puck to goal
    # First, put the gripper roughly above the puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper is above the puck but there is a wall in the way, move the
    # robot to the side of the wall so that it can grab the puck.
    if check("the robot's gripper is blocked by a wall"):
        robot.move_to("to the side of the wall")
    # Once the robot is in position, move the gripper above the puck and around
    # the wall to grab it.
    if check("the robot's gripper is not around the puck and the robot is near the puck"):
        robot.move_gripper("around the wall and near the puck", close_gripper=True)
    # If the gripper is near the target location and open, move the puck to the
    # goal.
    if check("the robot's gripper is near the target location and the robot's gripper is closed"):
        robot.move_gripper("near the target location")