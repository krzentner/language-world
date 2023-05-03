

if check("the robot's gripper is not vertically aligned with the wall"):
    robot.put("gripper on top of the wall")
if check("the robot's gripper is not close to the wall and the robot's gripper is forward aligned with the wall"):
    robot.move("gripper close to the wall")
if check("the robot's gripper is forward aligned with the wall and the robot's gripper is  not vertically aligned with the button"):
    robot.put("gripper above the button")
if check("the robot's gripper is vertically aligned with the button"):
    robot.push("down on the button")