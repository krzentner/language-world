

The robot should grab onto the wall and then reach to the target location.

# reach-wall: reach to the target location with a short wall in the way
# def reach_wall(robot):
    # Steps:
    #  1. Reach towards the wall
    #  2. Grab onto the wall with the gripper
    #  3. Reach towards the target
    
    # We want to grab onto the wall first, so we need to make sure the gripper is
    # near it.
    if check("the robot's gripper is not near the wall"):
        robot.move_gripper("near the wall")
    # Once the gripper is near the wall, try to grab it by closing the gripper.
    # Closing the gripper will also help stabilize the robot's movement.
    if check("the robot's gripper is near the wall and the robot's gripper is open"):
        robot.move_gripper("near the wall", close_gripper=True)
    # If the gripper is near the wall and closed, the robot should have a good
    # grip. Now it can move towards the target.
    if check("the robot's gripper is near the wall and the robot's gripper is closed"):
        robot.move_gripper("near the target")