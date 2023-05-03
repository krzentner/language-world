

The program for the `basketball` task: 

```
# basketball: put the ball into into the hoop
def basketball(robot):
  if check("the robot's gripper is not above ball"):
    robot.reach("above the ball")
    
  if check("the robot's gripper is not around ball and the robot's gripper is open"):
    robot.drop("gripper around ball")
  
  if check("the robot's gripper is near the ball and the robot's gripper is open"):
    robot.close("gripper around ball")
  
  if check("the robot's gripper is above ball and the robot's gripper is closed"):
    robot.put("ball above hoop")
    robot.push("ball through hoop")
```