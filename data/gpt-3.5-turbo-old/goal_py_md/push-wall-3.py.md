# push-wall: slide the puck to the target location with a small wall in the way
# def push_wall(robot):
    # Steps:
    #  1. Move the gripper above the puck
    #  2. Check if the wall is blocking the gripper's path to the puck 
    #  3. Move the gripper to the left or right of the wall, whichever is closer to the puck
    #  4. Lower the gripper onto the puck
    #  5. Move the gripper to the target location
    
    # First move the gripper above the puck
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
        
    # Check if the wall is blocking the path to the puck
    # If the wall is blocking the way to the puck, move the gripper 
    # to either side of the wall depending on which side is closer to the puck
    if check("there is a wall blocking the gripper's path to the puck"):
        distance_to_left = robot.distance_to_object("left side of the wall")
        distance_to_right = robot.distance_to_object("right side of the wall")
        
        if distance_to_left < distance_to_right:
            robot.move_gripper("left side of the wall")
        else:
            robot.move_gripper("right side of the wall")
    
    # Lower the gripper onto the puck
    if check("the robot's gripper is not close to the puck"):
        robot.move_gripper("near the puck", close_gripper=True)
    
    # Move the gripper to the target location
    if check("the robot's gripper is not above the target location"):
        robot.move_gripper("above the target location")