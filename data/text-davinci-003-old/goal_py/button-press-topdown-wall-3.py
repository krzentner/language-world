
    # Steps:
    #  1. Position above Wall, slightly left of button
    #  2. Move gripper down, around Wall and above button
    #  3. Push down from the top
    # First, we want to position the gripper over the wall slightly left of the button.
    if check("the robot's gripper is not above the wall and the robot's gripper is not left of the button"):
        robot.move_gripper("above the wall, slightly left of the button") 
    # The gripper should be slightly left of the button so that when it moves down it will easily move around the wall.
    # We then need to position the gripper down around the wall. 
    if check("the robot's gripper is not around the wall and the robot's gripper is open"):
        robot.move_gripper("around the wall", close_gripper=True)    
    # Finally, we need to push down on the button. 
    if check("the robot's gripper is around the wall and the robot's gripper is closed"):
        robot.move_gripper("above the button")