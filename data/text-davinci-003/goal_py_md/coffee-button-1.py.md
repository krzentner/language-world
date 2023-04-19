

Def coffee_button(robot): 
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    #  3. Move back up to initial position
    
    # First, place the gripper vertically aligned with the button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Once the gripper is lined up appropriately, push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button")
    # After pushing the button, move the gripper back to its initial position.
    if check("the robot's gripper is near the button"):
        robot.move_gripper("above the button")