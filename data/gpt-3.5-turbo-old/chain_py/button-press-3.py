# Steps:
#  1. Put gripper in front of button
#  2. Grab the button with the gripper
#  3. Push the button
# We need to put the gripper in front of the button first.
if check("the robot's gripper is not in front of the button"):
    robot.put("gripper in front of button")
# Once the gripper is lined up in front of the button, we can grab it.
if check("the robot's gripper is in front of button and the robot's gripper is not around button"):
    robot.grab("button")
# We have the button in our gripper now, so we can just push it.
if check("the robot's gripper is around button"):
    robot.push("button")