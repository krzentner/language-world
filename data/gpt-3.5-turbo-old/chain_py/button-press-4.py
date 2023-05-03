# Steps:
#  1. Line up the gripper as viewed from the front
#  2. Push the button
# Because this is just a front view, we just need to line up the gripper from
# the front. Line up the robot's gripper from the front. We don't need to be
# careful about how we're pushing the button, just push it.
if check("the robot's gripper is not forward aligned with the button"):
    robot.move("gripper in front of button")
if check("the robot's gripper is forward aligned with button"):
    robot.push("button")