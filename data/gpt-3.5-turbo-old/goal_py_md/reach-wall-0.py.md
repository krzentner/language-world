# reach-wall: reach to the target location with a short wall in the way
# def reach_wall(robot):
    # Steps:
    #  1. Check if there is a wall in the way
    #  2. Move to a position where the wall isn't in the way
    #  3. Reach towards the target
    # Check if there is a wall in the way between the robot and the target
    if check("there is a wall in the way between the robot and the target"):
        # Move the robot to a position where the wall isn't in the way 
        robot.move("to a position where the wall isn't in the way")
    # Reach towards the target
    robot.move_gripper("near the reach target")