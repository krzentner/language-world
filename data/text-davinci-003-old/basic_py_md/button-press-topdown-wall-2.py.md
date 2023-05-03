

if check("the robot's gripper is not near the button and the robot's gripper is not directly above the button"):
    robot.put("gripper directly above button")
if check("the robot's gripper is near the button and the robot's gripper is not above the wall blocking the button"):
    robot.put("gripper above the wall")
if check("the robot's gripper is above the wall and the robot's gripper is open"):
    robot.put("gripper above the button")
if check("the robot's gripper is above the button and the robot's gripper is open"):
    robot.close("gripper around the button")
if check("the robot's gripper is above the button and the robot's gripper is closed"):
    robot.push("down on the button")