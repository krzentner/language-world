

if check("the robot's gripper is not next to the wall and not vertically aligned with the button"):
    robot.put("gripper next to the wall above the button")
if check("the robot's gripper is vertically aligned with the button and not near the button"):
    robot.grab("gripper above the wall and push towards the button")
if check("the robot's gripper is near the button"):
    robot.push("button down")