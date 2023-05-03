

The robot needs to be able to reach through a wall in order to complete this task.

# reach-wall: reach to the target location with a short wall in the way
# def reach_wall(robot):
    # Steps:
    #  1. Reach towards the target location
    #  2. Push the wall
    #  3. Reach past the wall
    # We will need to maneuver around a wall to get to the target location. 
    # First we reach towards the target location. 
    if check("the robot's gripper is not near reach target"):
        robot.move_gripper("near the reach target")
    # To get past the wall, we need to move the gripper to the top of the wall,
    # pushing gently until it moves.
    if check("the robot's gripper is not above the wall"):
        robot.move_gripper("above the wall")
    # Now we can slide the gripper past the wall and reach the target.
    if check("the robot's gripper is not near the target"):
        robot.move_gripper("past the wall")