# reach-wall: reach to the target location with a short wall in the way
# def reach_wall(robot):
    # Steps:
    #  1. Check if there is a wall
    #  2. If there is a wall, move above the wall
    #  3. Move towards the target location
    #  4. Move down to the target location

    # Check if there is a wall
    if check("there is a wall between the robot's gripper and the target location"):
        # If there is a wall, move above it
        robot.move_gripper("above the wall")
    
    # Move towards the target location
    robot.move_gripper("near the target location")
    
    # Move down to the target location
    robot.move_gripper("at the target location")