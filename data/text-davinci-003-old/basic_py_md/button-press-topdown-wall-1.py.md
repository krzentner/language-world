

if check("the robot's gripper is not vertically aligned with button"):
   robot.reach("top of the wall") 
if check("the robot's gripper is not above button"):
   robot.put("gripper above the button") 
if check("the robot's gripper is above button and the robot is not on top of the wall"):
    robot.climb("onto the top of the wall")
if check("the robot's gripper is above button and the robot is on top of the wall"):
   robot.push("down on button")