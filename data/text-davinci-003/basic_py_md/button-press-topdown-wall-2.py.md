

if check("the robot's gripper is not vertically aligned with button"):
    robot.put("gripper above button")
if check("the robot's gripper is above the button, but there is a short wall in the way"):
    robot.put("gripper to the left or right side of the wall")
if check("the robot's gripper is just behind the wall and the wall is in front of the button"):
    robot.push("the wall away from the button")
if check("the robot's gripper is forward aligned with the button"):
    robot.push("the button down")