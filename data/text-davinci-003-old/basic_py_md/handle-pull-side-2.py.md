

Then add the code:
```	
    if check("the robot's gripper is not near the handle"):
        robot.move("gripper to left of handle")
    if check("the robot's gripper is near the handle and the robot's gripper is open"):
        robot.grab("handle")
    if check("the robot's gripper is near the handle and the robot's gripper is closed"):
        robot.pull("handle up")
```