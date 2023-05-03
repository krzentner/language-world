# reach-wall: reach to the target location with a short wall in the way
# def reach_wall(robot):
# Steps:
#  1. Check if there is a wall in front of the robot
#  2. If yes, move the robot to the side of the wall
#  3. Reach toward the target location
# Check if there is a wall in front of the robot
if check("there is a wall in front of the robot"):
    # If the wall is to the left of the robot, move to the right of the wall
    if check("the wall is to the left of the robot"):
        robot.move("right of wall")
    # If the wall is to the right of the robot, move to the left of the wall
    elif check("the wall is to the right of the robot"):
        robot.move("left of wall")
# Reach towards the target location
robot.reach("to goal")