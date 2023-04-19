

Steps:
1. Put gripper above the button
2. Lower the gripper down to the button
3. Push the button

if check("the robot's gripper is not above the button"):
    robot.put("gripper above button")
if check("the robot's gripper is not near the button"):
    robot.lower("gripper to button")
if check("the robot's gripper is near the button"):
    robot.push("button")