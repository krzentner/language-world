# Steps:
#  1. Put the gripper in front of the button
#  2. Push down on the button
# Move the gripper in front of the button.
if check("the robot's gripper is not almost horizontally aligned with the coffee machine button"):
    robot.move("gripper in front of the coffee machine button")
# Push down on the button.
if check("the robot's gripper is almost horizontally aligned with the coffee machine button"):
    robot.push("down on the coffee machine button")