# Steps:
    #  1. Line up the gripper with the button from above, but offset to the side
    #     to avoid the wall.
    #  2. Move the gripper directly above the button and push down.
    
    # First, position the gripper roughly above the button, but offset to the side
    # to avoid the wall.
    if check("the robot's gripper is not vertically aligned with button and is not offset from the wall"):
        robot.move_gripper("vertically aligned with the button and offset from the wall", close_gripper=True)
    # If the gripper is offset from the button and aligned with it from above,
    # move directly above the button and push down.
    if check("the robot's gripper is vertically aligned with button and is offset from the wall"):
        robot.move_gripper("above the button")