
    # Steps:
    #  1. Move the gripper to a position to the side of the puck, near the wall
    #  2. Drop the gripper around the puck
    #  3. Close the gripper around the puck
    #  4. Move the puck to the goal
    # The robot needs to move around the wall to get to the puck, so we have it
    # move to a position to the side of the puck near the wall.
    if check("the robot's gripper is not near the wall and puck"):
        robot.move_gripper("near the wall and puck")
    # The gripper should be able to drop to the puck from this position.
    if check("the robot's gripper is near the wall and puck and the robot's gripper is not around puck"):
        robot.move_gripper("below the puck")
    # If the gripper is around the puck but open, close it.
    if check("the robot's gripper is around the puck and the robot's gripper is open"):
        robot.move_gripper("near the wall and puck", close_gripper=True)
    # If the gripper is closed, we can move the puck to the target location.
    if check("the robot's gripper is around the puck and the robot's gripper is closed"):
        robot.move_gripper("near the target location")