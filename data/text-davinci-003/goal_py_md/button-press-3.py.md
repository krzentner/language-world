    

Then continue with the code:

    # Steps:
    #  1. Line up the gripper as viewed from in front
    #  2. Push the button from the front
    # We don't need to line up the gripper from above, so we can just get above
    # the button and the line the gripper up from in front. 
    if check("the robot's gripper is not forward aligned with button"):
        robot.move_gripper("forward aligned with the button", close_gripper=True)
    # Now that the gripper is lined up, just push the button.
    if check("the robot's gripper is forward aligned with button"):
        robot.move_gripper("near the button")