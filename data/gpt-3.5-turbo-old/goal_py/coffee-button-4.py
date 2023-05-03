# Steps:
#  1. Put gripper above the button
#  2. Push down on the button
# Similar to the button press task, we just need to line up the gripper above
# the button from above.
# Line up the robot's gripper from above.
if check("the robot's gripper is not vertically aligned with button"):
    robot.move_gripper("vertically aligned with the button", close_gripper=True)
# Now that the gripper is lined up, just push down on the button.
if check("the robot's gripper is vertically aligned with button"):
    robot.move_gripper("near the button")