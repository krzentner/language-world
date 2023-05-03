

If check("the robot's gripper is not vertically aligned with button"):
    robot.put("gripper above wall")
if check("the robot's gripper is above the wall and not vertically aligned with button"):
    robot.move("gripper above button")
if check("the robot's gripper is not above the button and not vertically aligned with button"):
    robot.put("gripper on the wall")
if check("the robot's gripper is above the button"):
    robot.push("down on button")