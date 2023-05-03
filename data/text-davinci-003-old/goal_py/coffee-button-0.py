
    # Steps:
    #  1. Put gripper left of button
    #  2. Place gripper around button 
    #  3. Push button
    # First, if the gripper isn't close to the button, move it there.
    # We don't need to worry about the angle, since the button is big.
    if check("the robot's gripper is not near the button"):
        robot.move_gripper("near the button")
    # If the gripper is around the button, but the button is still not lined up
    # with the gripper as viewed from above, move the gripper so that it is.
    if check("the robot's gripper is not vertically aligned with button and the robot's gripper is closed"):
        robot.move_gripper("vertically aligned with the button")
    # If the gripper is lined up with the button, push the button.
    if check("the robot's gripper is vertically aligned button"):
        robot.move_gripper("above the button")