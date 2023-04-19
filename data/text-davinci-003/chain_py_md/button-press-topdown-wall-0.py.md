

Steps:
1. Find a way to get the gripper above the wall
2. Put the gripper above the button
3. Push down on the button from the top

if check("the robot's gripper is not above the wall"):
    robot.place("gripper above wall")
if check("the robot's gripper is above the wall and the robot's gripper is not above the button"):
    robot.place("gripper above button")
if check("the robot's gripper is above the button"):
    robot.push("down on button")