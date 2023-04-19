

Once the gripper is near the wall, the robot should reach around it.

# reach-wall: reach to the target location with a short wall in the way
# def reach_wall(robot):
    # Steps:
    #  1. Reach towards the wall
    #  2. Reach around the wall
    #  3. Reach to the target
    # 
    # First, reach towards the wall. We don't have any objects to manipulate, so
    # we can just move the robot's gripper directly to the wall.
    if check("the robot's gripper is not near the wall"):
        robot.move_gripper("near the wall")
    # Now that the gripper is near the wall, position the gripper so that it is
    # parallel to the wall and reach around it.
    if check("the robot's gripper is not parallel to the wall"):
        robot.move_gripper("parallel to the wall")
    # Now that the gripper is parallel to the wall, move it around the wall to
    # the target.
    if check("the robot's gripper is not near the target"):
        robot.move_gripper("around the wall to the target")