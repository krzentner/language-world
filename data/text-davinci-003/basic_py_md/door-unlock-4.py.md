

Then add the following code:

```
    if check("the robot's gripper is not near the dial"):
        robot.reach("to dial")
 
    if check("the robot's gripper is near the dial and the dial is not at the goal"):
        robot.turn("dial to goal")
        
    if check("the dial is at the goal"):
        robot.pull("door open")
```