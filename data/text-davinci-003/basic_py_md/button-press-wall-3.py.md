

This code should allow the robot to press a button from the front with a short wall in the way.

if check("the robot's gripper is not forward aligned with button and there is an obstacle in between"):
    robot.turn("to put gripper in line with button and the wall")
if check("the robot's gripper is forward aligned with button and the robot's gripper is not close to button"):
    robot.move("gripper near button")
if check("the robot's gripper is close to button"):
    robot.push("button through wall")