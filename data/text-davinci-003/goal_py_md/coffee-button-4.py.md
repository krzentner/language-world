

Then, the program should follow the same steps as the other tasks:

# Steps:
#  1. Line up the gripper as viewed from above
#  2. Push down on the button from the top
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button")