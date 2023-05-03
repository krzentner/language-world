# reach-wall: reach to the target location with a short wall in the way
def reach_wall(robot):
    # Steps:
    #  1. Check if there is a wall in front of the robot
    #  2. If there is a wall, move the robot's gripper around to the side of the wall
    #  3. Move the robot's gripper to the target location
    # First, check if there is a wall in front of the robot.
    if check("there is a wall in front of the robot"):
        # If there is a wall, move the robot's gripper around to the side of the wall.
        robot.move_gripper("around the short wall", close_gripper=True)
    # Move the robot's gripper to the target location.
    if check("the robot's gripper is not near the reach target"):
        robot.move_gripper("near the reach target")